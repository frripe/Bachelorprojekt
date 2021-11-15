# python3 run.py -t -q -f 0.02
# python3 run.py -t -f 0.3 -i ../dataset/training/jpg/Blurry/

import os
import sys
import argparse

from choose_threshold import find_threshold
from compute_scores import compute_scores
from compute_scores import compute_score
from webcam_app import run_webcam_application

from metrics_and_training_code.visualize_output import retrieve_metric_name
from metrics_and_training_code.visualize_output import plot_box
from metrics_and_training_code.visualize_output import plot_conf
from metrics_and_training_code.visualize_output import init_y
from metrics_and_training_code.visualize_output import y_predicted

def _parse_args():
    parser = argparse.ArgumentParser(description='run blur detection on test images')
    parser.add_argument('-t', '--test', action='store_true', help='run on test data set and plot output')
    parser.add_argument('-q', '--quick', action='store_true', help='use the fastest metric instead of the most accurate')
    parser.add_argument('-f', '--fpr', type=float, default=0.1, help='tolerable FPR, default 10%')
    parser.add_argument('-i', '--image_path', type=str, help='directory of images')
    # parser.set_defaults(test='spam')
    return parser.parse_args()

def _plot_output(threshold, scores, metric, fpr, quick, path=0):
    blurry = scores['Blurry'] + scores['synth_blurry']
    sharp  = scores['NoProblems_no_outlier'] + scores['synth_no_problems_no_outlier']
    y_true, y_score = init_y(blurry, sharp)
    y_pred = y_predicted(threshold, blurry, sharp)
    if path:
        plot_box('', retrieve_metric_name(metric)[0], '', sharp, blurry, scores['synth_blurry_2.0'], scores['synth_blurry_3.0'], scores['synth_blurry_4.0'], fpr, 3, quick)
        plot_conf(y_true, y_pred, threshold, fpr, quick, 3)
    else:
        plot_box('', retrieve_metric_name(metric)[0], '', sharp, blurry, scores['synth_blurry_2.0'], scores['synth_blurry_3.0'], scores['synth_blurry_4.0'], fpr, 2, quick)
        plot_conf(y_true, y_pred, threshold, fpr, quick, 2)

if __name__ == '__main__':
    # assert sys.version_info >= (3, 6), sys.version_info
    args = _parse_args()
    threshold, metric = find_threshold(args.fpr, args.quick)
    print('threshold ' + str(threshold))
    print('metric    ' + str(metric))
    print('fpr       ' + str(args.fpr))

    hf = 'metrics_and_training_code/Histogram-Frequency-based/output/'
    test_data = '../dataset/test/jpg/'

    if args.test:
        if args.image_path:
            for path in args.image_path:
                if args.quick:
                    if path == '.':
                        scores = compute_scores(hf, args.image_path)
                    else:
                        scores = compute_scores(hf, path)
                else:
                    if path == '.':
                        scores = compute_scores(metric, args.image_path)
                    else:
                        scores = compute_scores(metric, path)
                print(scores)
                if(path in [test_data, '../dataset/training/jpg/', '../dataset/test/png/', '../dataset/training/png/']):
                    _plot_output(threshold, scores, metric, args.fpr, args.quick, 1)
        else:
            if args.quick:
                scores = compute_scores(hf, test_data)
            else:
                scores = compute_scores(metric, test_data)
            print(scores)
            _plot_output(threshold, scores, metric, args.fpr, args.quick)
    else: # run on input image from webcam
        os.makedirs('app_blurry_images/', exist_ok=True)
        os.makedirs('app_sharp_images/', exist_ok=True)
        run_webcam_application(args.quick, args.fpr, threshold, metric)
