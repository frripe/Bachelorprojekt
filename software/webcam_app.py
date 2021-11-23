import cv2
import os
import PySimpleGUI as sg
import queue
import tempfile
import time
from multiprocessing import Process, Queue, Value # https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue
from PIL import Image

import metrics
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

def _set_threshold_and_metric(fpr, quick, threshold, metric):
    a, b = find_threshold(fpr, quick)
    with threshold.get_lock():
        with metric.get_lock():
            threshold.value, metric.value = a, b

def _run(quick, fpr, window, vcap, sharp_images_stored, thresh, metr):
    threshold = Value('f', thresh)
    metric    = Value('d', metr)
    imgQueue  = Queue(8)
    computing = False
    load      = False

    p = Process(target=_classify_images, args=(imgQueue, threshold, metric, sharp_images_stored))
    p.start()

    last_image_time = time.time()
    while(1):
        event, values = window.Read(timeout=20, timeout_key='timeout') # get events for the window with 20ms max wait
        if event is None:
            _soft_end(imgQueue, p)
            p.join()
            p.close()
            print("breaking")
            break # if user closed window, quit
        if event == 'Fast':
            quick = True
            _set_threshold_and_metric(fpr, quick, threshold, metric)
            window['metric'].update('\nUsing fastest classifier')
        if event == 'Accurate':
            quick = False
            _set_threshold_and_metric(fpr, quick, threshold, metric)
            window['metric'].update('\nUsing most accurate classifier')
        if event == 'slider':
            new_fpr = values['slider']/100
            print("new_fpr: " + str(new_fpr))
            if fpr != new_fpr:
                fpr = new_fpr
                _set_threshold_and_metric(fpr, quick, threshold, metric)

        if event == "Load Image":
            load = True
            computing = False
            window['on_off'].update('(paused)')
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = cv2.imread(values["-FILE-"])
                window.find_element('image').Update(data=cv2.imencode('.png', image)[1].tobytes())
                res = _is_sharp(compute_score(metric.value, values["-FILE-"]), threshold.value)
                window['result'].update('Sharp: ' + str(res))
        if event == 'Start':
            if not load:
                computing = True
                window['on_off'].update('(on)')
            else:
                window['result'].update('')
                load = False
        if event == 'Pause':
            computing = False
            window['on_off'].update('(paused)')

        if not load:
            grabbed, frame = vcap.read()
            image_time = time.time()

            if grabbed is False :
                print('[Exiting] No more frames to read')
                _soft_end(imgQueue, p)
                p.join()
                p.close()
                load = True
                computing = False
            else:
                window.find_element('image').Update(data=cv2.imencode('.png', frame)[1].tobytes())
                window['sharp_images_stored'].update('Sharp images stored: ' + str(round(sharp_images_stored.value)))
                if computing and image_time-last_image_time > .5: # half a second between images to classify
                    imgQueue.put_nowait(frame)
                    last_image_time = image_time

def run_webcam_application(quick, fpr, threshold, metric):
    vcap = cv2.VideoCapture(0)
    if vcap.isOpened() is False :
        print("[Exiting]: Error accessing webcam stream.")
        exit(0)

    sharp_images_stored = Value('d', 0)
    sg.theme('Dark Blue 2')
    q_metric = sg.Text('\nUsing fastest classifier', font=('Helvetica 10'), key='metric') if quick else sg.Text('\nUsing most accurate classifier', font=('Helvetica 10'), key='metric')
    layout_cam  = [[sg.Image(filename='', key='image')]]
    layout_menu = [
        [sg.Text('Load image file or use webcam', font=('Helvetica 12'))],

        [sg.Text('Compute sharpness of webcam input:', font=('Helvetica 10'))],
        [sg.Text('Sharp images stored: ' + str(round(sharp_images_stored.value)), font=('Helvetica 10'), key='sharp_images_stored')],
        [
        sg.Button('Start'),
        sg.Button('Pause'),
        sg.Text('(paused)', font=('Helvetica 10'), key='on_off')
        ],

        # [sg.Image(key="-IMAGE-")],
        [sg.Text("\nCompute sharpnes of image file:")],
        [
        sg.Input(size=(16, 1), key="-FILE-"),
        sg.FileBrowse(file_types=[("JPEG", "*.jpg"), ("JPEG", "*.jpeg"), ("PNG", "*.png"), ("Bitmap", "*.bmp"), ("All files", "*.*")])
        ],
        [sg.Button("Load Image"), sg.Text('', font=('Helvetica 10'), key='result')],

        [sg.Text('Classifier parameters', font=('Helvetica 12'))],
        [sg.Text('Acceptable percentage of blurry\nimages classified as sharp (%):', font=('Helvetica 10'))],
        [
        sg.Slider(range=(0, 100), orientation='h', size=(20,20), change_submits=True, key='slider',
        font=('Helvetica 10'), default_value=fpr*100),
        ],

        [q_metric],
        [sg.Button('Fast'), sg.Button('Accurate')],
            ]
    layout = [[
        sg.Column(layout_cam, element_justification='left'),
        sg.Column(layout_menu, element_justification='left'),
        # sg.Column(layout_menu2, element_justification='left')
        ]]
    window = sg.Window('Blur Detection - Demo Application', layout, location=(0,0))
    _run(quick, fpr, window, vcap, sharp_images_stored, threshold, metric)
    # exit(0)
