# python3 run.py -q 1

import os
import sys
import argparse
import subprocess
import cv2
import imageio
from PIL import Image

import cpbd
from choose_threshold import find_threshold
from metrics_and_training_code.laplacian_variance.blur_detection.detection import estimate_blur

from metrics_and_training_code.visualize_output import plot_box
from metrics_and_training_code.visualize_output import plot_conf
from metrics_and_training_code.visualize_output import init_y
from metrics_and_training_code.visualize_output import y_predicted


def _parse_args():
    parser = argparse.ArgumentParser(description='run blur detection on test images')
    parser.add_argument('-i', '--image_path', type=str, nargs='+', help='image path - if excluded run on test data set and plot output')
    parser.add_argument('-f', '--fpr', type=float, default=0.1, help='tolerable FPR, default 10%')
    parser.add_argument('-q', '--quick', type=int, help='use the fastest metric instead of the most accurate')
    # parser.add_argument('-t', '--test', action='test', help='run on test data set and plot output')
    return parser.parse_args()

def _comp_lv(img):
    if 'png' in img or 'jpg' in img:
        image = cv2.imread(img)
        return float(estimate_blur(image)[1])
    # format image
    image = Image.open(img)
    img = os.path.splitext(img)[0] + '.png'
    image.save(img)
    image = cv2.imread(img)
    score = float(estimate_blur(image)[1])
    os.remove(img)
    return score

def _comp_hf(img):
    print(img)
    if 'jpg' in img:
        score = float(subprocess.check_output(['./metrics_and_training_code/Histogram-Frequency-based/marichal-ma-zhang', '-d=1', '-h=0.085', '-t=0', img]).decode())
        print(score)
        return score
    # format image
    image = Image.open(img)
    img = os.path.splitext(img)[0] + '.jpg'
    image.save(img)
    score = float(subprocess.check_output(['./metrics_and_training_code/Histogram-Frequency-based/marichal-ma-zhang', '-d=1', '-h=0.085', '-t=0', img]).decode())
    os.remove(img)
    return score

def _comp_cpbd(img):
    # TODO: format image
    if 'bmp' in img:
        img = imageio.imread(img, pilmode='L')
        return float(cpbd.compute(img))
    # format image
    image = Image.open(img)
    img = os.path.splitext(img)[0] + '.bmp'
    image.save(img)
    image = imageio.imread(img, pilmode='L')
    score = float(cpbd.compute(image))
    os.remove(img)
    return score

def compute_scores(metric, directory):
    paths = os.listdir(directory)
    all_scores = {}
    for path in paths:
        scores = []
        images = os.listdir('../dataset/test/jpg/' + path + '/')
        for img in images:
            # print(compute_score(metric, directory + path + '/'+ img))
            scores.append(compute_score(metric, directory + path + '/'+ img))
        # print(scores)
        all_scores[path] = scores
    return all_scores

def compute_score(metric, image_path):
    if metric == 'metrics_and_training_code/laplacian_variance/output/jpg/':
        return _comp_lv(image_path)
    if metric == 'metrics_and_training_code/Histogram-Frequency-based/output/':
        return _comp_hf(image_path)
    if metric == 'metrics_and_training_code/cpbd/output/':
        return _comp_cpbd(image_path)
    if metric == 'metrics_and_training_code/merge_metrics/cpbd_lv_jpg/many_alpha/alpha_4/':
        return .4*_comp_cpbd(image_path) + .6*_comp_lv(image_path)
    if metric == 'metrics_and_training_code/merge_metrics/cpbd_HF/many_alpha/alpha_2/':
        return .2*_comp_cpbd(image_path) + .8*_comp_lv(image_path)
    if metric == 'metrics_and_training_code/merge_metrics/HF_lv_jpg/many_alpha/alpha_7/':
        return .7*_comp_cpbd(image_path) + .3*_comp_lv(image_path)
    if metric == 'metrics_and_training_code/merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_4_1/':
        return .4*_comp_cpbd(image_path) + .1*_comp_hf(image_path) + .5*_comp_lv(image_path)

def _is_sharp(threshold, score):
    print('blurry') if bool(score < threshold) else print('sharp')

def _plot_output(scores):
    blurry = scores['Blurry'] + scores['synth_blurry']
    sharp  = scores['NoProblems'] + scores['synth_no_problems']
    y_true, y_score = init_y(blurry, sharp)
    y_pred = y_predicted(threshold, blurry, sharp)
    plot_box('', '', '', sharp, blurry, scores['synth_blurry_2.0'], scores['synth_blurry_3.0'], scores['synth_blurry_4.0'], save=0)
    plot_conf(y_true, y_pred, threshold)

if __name__ == '__main__':
    args = _parse_args()
    threshold, metric = find_threshold(args.fpr, args.quick)
    print('threshold ' + str(threshold))
    print('metric ' + str(metric))

    if not args.image_path:
        if args.quick:
            scores = compute_scores('metrics_and_training_code/Histogram-Frequency-based/output/', '../dataset/test/jpg/')
        else:
            scores = compute_scores(metric, '../dataset/test/jpg/')
        print(scores)
        _plot_output(scores)
    else:
        # TODO: run on input image from webcam
        while(1):
            if args.quick:
                _is_sharp(threshold, compute_score('Histogram-Frequency-based/output/', ...))
            else:
                _is_sharp(threshold, compute_score(metric, ...))
