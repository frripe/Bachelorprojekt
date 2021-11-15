import cv2
import metrics
import os
import PySimpleGUI as sg
import queue
import tempfile
import time
from multiprocessing import Process, Queue, Value # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue
from choose_threshold import find_threshold
from compute_scores import compute_score

def _is_sharp(score, threshold):
    print("score: " + str(score))
    return False if bool(score < threshold) else True

def _compute(frame, threshold, metric, sharp_images_stored):
    print("computing)")
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = tmpdirname + '/img.png'
        cv2.imwrite(path, frame)
        if _is_sharp(compute_score(metric, path), threshold):
            p = 'app_sharp_images/'
            print("sharp: ", str(len(os.listdir(p))) + '.png')
            cv2.imwrite(str(p) + str(len(os.listdir(p))) + '.png', frame)
            sharp_images_stored.value += 1
        else:
            p = 'app_blurry_images/'
            print("blurry: " + str(len(os.listdir(p))) + '.png')
            cv2.imwrite(str(p) + str(len(os.listdir(p))) + '.png', frame)

def _soft_end(imgQueue, process):
    imgQueue.put(False)

def _classify_images(imgQueue, threshold, metric, sharp_images_stored):
    print("classifier process started...")
    while(1):
        frame = imgQueue.get()
        print("                         queue size: " + str(imgQueue.qsize()))
        if isinstance(frame, bool): # false added to queue for shutdown
            break
        with threshold.get_lock():
            with metric.get_lock():
                t, m = threshold.value, metric.value
        print("processing image, " + str(t))
        _compute(frame, t, m, sharp_images_stored)

def _run(quick, fpr, window, vcap, sharp_images_stored, thresh, metr):
    threshold  = Value('f', thresh)
    metric     = Value('d', metr)
    imgQueue   = Queue(8)

    p = Process(target=_classify_images, args=(imgQueue, threshold, metric, sharp_images_stored))
    p.start()

    computing = False
    last_image_time = time.time()
    while(1):
        event, values = window.Read(timeout=20, timeout_key='timeout') # get events for the window with 20ms max wait
        if event is None:
            _soft_end(imgQueue, p)
            p.join()
            window['sharp_images_stored'].update('\nSharp images stored: ' + str(round(sharp_images_stored.value)))
            p.close()
            print("breaking")
            break # if user closed window, quit
        if event == 'Start':
            computing = True
        if event == 'Pause':
            computing = False
        if event == 'slider':
            new_fpr = values['slider']/100
            print("new_fpr: " + str(new_fpr))
            if fpr != new_fpr:
                fpr = new_fpr
                a, b = find_threshold(fpr, quick)
                with threshold.get_lock():
                    with metric.get_lock():
                        threshold.value, metric.value = a, b
        grabbed, frame = vcap.read()
        image_time = time.time()
        window.find_element('image').Update(data=cv2.imencode('.png', frame)[1].tobytes())

        if grabbed is False :
            print('[Exiting] No more frames to read')
            _soft_end(imgQueue, p)
            p.join()
            p.close()
            break
        if computing and image_time-last_image_time > .5: # half a second between images to classify
            imgQueue.put_nowait(frame)
            last_image_time = image_time
        window['sharp_images_stored'].update('\nSharp images stored: ' + str(round(sharp_images_stored.value)))

def run_webcam_application(quick, fpr, threshold, metric):
    vcap = cv2.VideoCapture(0)
    # vcap = cv2.VideoCapture(2) # cam 2
    if vcap.isOpened() is False :
        print("[Exiting]: Error accessing webcam stream.")
        exit(0)

    # print("W: " + str(vcap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    # print("H: " + str(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # vcap.set(cv2.CAP_PROP_FRAME_WIDTH, 455)
    # vcap.set(cv2.CAP_PROP_FRAME_HEIGHT, 455)

    sharp_images_stored = Value('d', 0)
    sg.theme('Dark Blue 2')
    layout_cam  = [[sg.Image(filename='', key='image')]]
    layout_menu = [
        [sg.Text('Acceptable percentage of blurry\nimages classified as sharp:', font=('Helvetica 11'))],
        [sg.Slider(range=(0, 100), orientation='h', size=(20,20), change_submits=True, key='slider',
            font=('Helvetica 10'), default_value=fpr*100)],
        [sg.Text('Compute sharpness:', font=('Helvetica 10'))],
        [sg.Button('Start'), sg.Button('Pause')],
        [sg.Text('\nSharp images stored: ' + str(round(sharp_images_stored.value)), font=('Helvetica 10'), key='sharp_images_stored')],
            ]
    layout = [[
        sg.Column(layout_cam, element_justification='center'),
        sg.Column(layout_menu, element_justification='center')
        ]]
    window = sg.Window('Blur Detection - Demo Application', layout, location=(0,0))
    _run(quick, fpr, window, vcap, sharp_images_stored, threshold, metric)
    exit(0)
