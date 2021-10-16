# python3 merge_metrics/merge_data.py cpbd/output/ laplacian_variance/output/ merge_metrics/cpbd_lv/out_alpha
import os
import sys
import imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
from scipy.stats import norm

# folder with outputs
path1 = sys.argv[1]
path2 = sys.argv[2]
path3 = sys.argv[3]
alpha = float(sys.argv[4])

def open_scores(path, file_name):
    with open(path + file_name) as f:
        scores = [float(s) for s in f]
        f.close()
    return scores

def comp_scores(scores1, scores2):
    a = alpha/10
    scores = []
    for s1, s2 in zip(scores1, scores2):
        scores.append(a*s1 + (1-a)*s2)
    return scores

def comp_times(times1, times2):
    return [t1+t2 for t1, t2 in zip(times1, times2)]

def write_to_file(scores, path, file_name):
    f = open(path + file_name, mode='wt', encoding='utf-8')
    for s in scores:
        f.write(str(s) + '\n')

scores1 = open_scores(path1, 'out_blurry.txt')
scores2 = open_scores(path2, 'out_blurry.txt')
scores  = comp_scores(scores1, scores2)
write_to_file(scores, path3, 'out_blurry.txt')

scores1 = open_scores(path1, 'out_synth_blurry.txt')
scores2 = open_scores(path2, 'out_synth_blurry.txt')
scores  = comp_scores(scores1, scores2)
write_to_file(scores, path3, 'out_synth_blurry.txt')

scores1 = open_scores(path1, 'out_no_problems.txt')
scores2 = open_scores(path2, 'out_no_problems.txt')
scores  = comp_scores(scores1, scores2)
write_to_file(scores, path3, 'out_no_problems.txt')

scores1 = open_scores(path1, 'out_synth_no_problems.txt')
scores2 = open_scores(path2, 'out_synth_no_problems.txt')
scores  = comp_scores(scores1, scores2)
write_to_file(scores, path3, 'out_synth_no_problems.txt')

times1 = open_scores(path1, 'time.txt')
times2 = open_scores(path2, 'time.txt')
times  = comp_times(times1, times2)
write_to_file(times, path3, 'time.txt')
