import cv2
import os
import PySimpleGUI as sg
import queue
import tempfile
import time
from multiprocessing import Lock, Process, Queue, Value # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue
from choose_threshold import find_threshold
from compute_scores import compute_score

# queueLock = Lock()
# imgQueue  = Queue(8)
threshold = 0
metric    = ''

def _is_sharp(score):
    print("score: " + str(score))
    return False if bool(score < threshold) else True

def _compute(frame):
    with tempfile.TemporaryDirectory() as tmpdirname:
        # print('created temporary directory', tmpdirname)
        path = tmpdirname + '/img.png'
        cv2.imwrite(path, frame)
        # print(metric)
        if _is_sharp(compute_score(metric, path)):
            # ++sharp_images_stored
            p = 'app_sharp_images/'
            print(p)
            cv2.imwrite(str(p) + str(len(os.listdir(p))) + '.png', frame)
            print("sharp")
        else:
            p = 'app_blurry_images/'
            cv2.imwrite(str(p) + str(len(os.listdir(p))) + '.png', frame)
            print("blurry")
    # return sharp_images_stored

def _soft_end(queueLock, imgQueue, process):
    # global imgQueue
    # global exitFlag
    while(1):
        queueLock.acquire()
        if imgQueue.empty():
            break
        queueLock.release()
        # print("ending: " + str(imgQueue.qsize()))
        # pass
    print("done")
    return 1

def _classify_images(queueLock, imgQueue, exitFlag):
    # global queueLock
    # global imgQueue
    # global exitFlag
    print("process started...")
    while(1):
        queueLock.acquire()
        print(imgQueue.qsize())
        if not imgQueue.empty():
            frame = imgQueue.get()
            queueLock.release()
            print("processing image")
            _compute(frame)
        else:
            queueLock.release()
            time.sleep(.5)
        if exitFlag.value:
            print("breaking process")
            break
    #     print(exitFlag.value)
    # print(exitFlag.value)

def _run(quick, fpr, window, vcap, sharp_images_stored):
    global threshold
    global metric
    queueLock = Lock()
    imgQueue = Queue(8)
    exitFlag = Value('b', False)

    p = Process(target=_classify_images, args=(queueLock, imgQueue, exitFlag))
    p.start()

    computing = False
    last_image_time = time.time()
    while(1):
        event, values = window.Read(timeout=20, timeout_key='timeout') # get events for the window with 20ms max wait
        if event is None:
            exitFlag.value = _soft_end(queueLock, imgQueue, p)
            # print("flag: " + str(exitFlag))
            print("breaking")
            break # if user closed window, quit
        if event == 'Start':
            computing = True
        if event == 'Pause':
            computing = False
        if event == 'slider':
            # print(event, values)
            new_fpr = values['slider']/100
            print(new_fpr)
            if fpr != new_fpr:
                fpr = new_fpr
                threshold, metric = find_threshold(fpr, quick)
                print(threshold, metric)

        grabbed, frame = vcap.read()
        image_time = time.time()
        window.find_element('image').Update(data=cv2.imencode('.png', frame)[1].tobytes())

        if grabbed is False :
            print('[Exiting] No more frames to read')
            exitFlag.value = _soft_end(queueLock, imgQueue, p)
            break

        if computing and image_time-last_image_time > .5: # half a second between images to classify
            # TODO: if timing, add new image to queue
            queueLock.acquire()
            # print(imgQueue.qsize())
            if not imgQueue.full():
                imgQueue.put(frame)
            queueLock.release()
            last_image_time = image_time
            # sharp_images_stored = _compute(threshold, metric, frame, sharp_images_stored)

def run_webcam_application(quick, fpr, thresh, metr):
    # print("metr: ", str(metr))
    global threshold
    global metric
    threshold = thresh
    metric = metr
    vcap = cv2.VideoCapture(0)
    if vcap.isOpened() is False :
        print("[Exiting]: Error accessing webcam stream.")
        exit(0)

    sharp_images_stored = 0
    sg.theme('Dark Blue 2')
    layout_cam  = [[sg.Image(filename='', key='image')]]
    layout_menu = [
        [sg.Text('Acceptable percentage of blurry\nimages classified as sharp:', font=('Helvetica 11'))],
        [sg.Slider(range=(0, 100), orientation='h', size=(20,20), change_submits=True, key='slider',
            font=('Helvetica 10'), default_value=fpr*100)],
        [sg.Text('Compute sharpness:', font=('Helvetica 10'))],
        [sg.Button('Start'), sg.Button('Pause')],
        [sg.Text('\nSharp images stored: ' + str(sharp_images_stored), font=('Helvetica 10'))],
            ]
    layout = [[
        sg.Column(layout_cam, element_justification='center'),
        sg.Column(layout_menu, element_justification='center')
        ]]
    window = sg.Window('Blur Detection - Demo Application', layout, location=(0,0))
    _run(quick, fpr, window, vcap, sharp_images_stored)
