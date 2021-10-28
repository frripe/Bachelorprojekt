# python3 merge_metrics/merge_data.py cpbd/output/ laplacian_variance/output/ merge_metrics/cpbd_lv/out_alpha
import os
import sys
import imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
from scipy.stats import norm

# folder with outputs
path1     = sys.argv[1]
path2     = sys.argv[2]
path3     = sys.argv[3]
save_path = sys.argv[4]
alpha     = float(sys.argv[5])
beta      = float(sys.argv[6])

def open_scores(path, file_name):
    with open(path + file_name) as f:
        scores = [float(s) for s in f]
        f.close()
    return scores

def comp_scores(scores1, scores2, scores3):
    a = alpha/10
    b = beta/10
    scores = []
    for s1, s2, s3 in zip(scores1, scores2, scores3):
        scores.append((a*s1 + beta*s2 + (1-a-b)*s3))
    return scores

def comp_times(times1, times2, times3):
    return [t1+t2+t3 for t1, t2, t3 in zip(times1, times2, times3)]

def write_to_file(scores, path, file_name):
    f = open(path + file_name, mode='wt', encoding='utf-8')
    for s in scores:
        f.write(str(s) + '\n')

def save_scores_for_file(filename):
    scores1 = open_scores(path1, filename)
    scores2 = open_scores(path2, filename)
    scores3 = open_scores(path3, filename)
    scores  = comp_scores(scores1, scores2, scores3)
    write_to_file(scores, save_path, filename)


for filename in ['out_blurry.txt', 'out_synth_blurry.txt', 'out_no_problems.txt',
                 'out_synth_no_problems.txt', 'out_synth_blurry_gaussian_2.0.txt',
                 'out_synth_blurry_gaussian_3.0.txt', 'out_synth_blurry_gaussian_4.0.txt']:
    save_scores_for_file(filename)

times1 = open_scores(path1, 'time.txt')
times2 = open_scores(path2, 'time.txt')
times3 = open_scores(path3, 'time.txt')
times  = comp_times(times1, times2, times3)
write_to_file(times, save_path, 'time.txt')
