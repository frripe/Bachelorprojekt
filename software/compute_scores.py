import os
import subprocess
import cv2
import imageio
from PIL import Image

import cpbd
from metrics_and_training_code.laplacian_variance.blur_detection.detection import estimate_blur
from metrics_and_training_code.laplacian_variance.blur_detection.detection import fix_image_size


extra_img_path = 'extra_images/'

def _comp_lv(img):
    if 'png' in img or 'jpg' in img:
        image = cv2.imread(img)
        image = fix_image_size(image)
        score = float(estimate_blur(image)[1])
        # print('lv   ', str(score))
        return score
    # format image
    image = Image.open(img)
    img = extra_img_path + os.path.splitext(os.path.basename(img))[0] + '.png'
    image.save(img)
    image = cv2.imread(img)
    image = fix_image_size(image)
    score = float(estimate_blur(image)[1])
    os.remove(img)
    return score

def _comp_hf(img):
    if 'jpg' in img:
        score = float(subprocess.check_output(['./metrics_and_training_code/Histogram-Frequency-based/marichal-ma-zhang', '-d=1', '-h=0.085', '-t=0', img]).decode())
        print('hf   ', str(score))
        return score
    # format image
    image = Image.open(img)
    img = extra_img_path + os.path.splitext(os.path.basename(img))[0] + '.jpg'
    image.save(img)
    score = float(subprocess.check_output(['./metrics_and_training_code/Histogram-Frequency-based/marichal-ma-zhang', '-d=1', '-h=0.085', '-t=0', img]).decode())
    os.remove(img)
    return score

def _comp_cpbd(img):
    if 'bmp' in img:
        img = imageio.imread(img, pilmode='L')
        score = float(cpbd.compute(img))
        # print('cpbd ', str(score))
        return score
    # format image
    image = Image.open(img)
    img = extra_img_path + os.path.splitext(os.path.basename(img))[0] + '.bmp'
    image.save(img)
    image = imageio.imread(img, pilmode='L')
    score = float(cpbd.compute(image))
    os.remove(img)
    print('cpbd ', str(score))
    return score

def compute_scores(metric, directory):
    content = os.listdir(directory)
    paths = [path for path in content if os.path.isdir(directory + path)]
    all_scores = {}
    if len(paths) > 0:
        for path in paths:
            scores = []
            images = os.listdir(directory + path + '/')
            for img in images:
                score = compute_score(metric, directory + path + '/'+ img)
                print(score)
                scores.append(score)
            all_scores[path] = scores
        return all_scores
    scores = []
    for img in content:
        score = compute_score(metric, directory + img)
        print(score)
        scores.append(score)
    return scores

def compute_score(metric, image_path):
    print(image_path)
    if metric == 'metrics_and_training_code/laplacian_variance/output/jpg/':
        return _comp_lv(image_path)
    if metric == 'metrics_and_training_code/Histogram-Frequency-based/output/':
        return _comp_hf(image_path)
    if metric == 'metrics_and_training_code/cpbd/output/':
        return _comp_cpbd(image_path)
    if metric == 'metrics_and_training_code/merge_metrics/cpbd_lv_jpg/many_alpha/alpha_4/':
        return .4*_comp_cpbd(image_path) + .6*_comp_lv(image_path)
    if metric == 'metrics_and_training_code/merge_metrics/cpbd_HF/many_alpha/alpha_2/':
        return .2*_comp_cpbd(image_path) + .8*_comp_hf(image_path)
    if metric == 'metrics_and_training_code/merge_metrics/HF_lv_jpg/many_alpha/alpha_7/':
        return .7*_comp_hf(image_path) + .3*_comp_lv(image_path)
    if metric == 'metrics_and_training_code/merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_2_6/':
        return .2*_comp_cpbd(image_path) + .6*_comp_hf(image_path) + .2*_comp_lv(image_path)
