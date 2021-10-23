# python3 visualize_output.py cpbd/output/
import os
import sys
import imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
from scipy.stats import norm

# folder with outputs
path = sys.argv[1]
p_name = '_' + path.replace('/', '-')

with open(path + 'time.txt') as f:
    times = [float(t) for t in f]
    f.close()
avg_time = str(round(sum(times)/len(times), 4))

if("laplacian_variance/output/" in path):
    title = "Laplacian Variance metric"
    name  = 'lv'
    # xmax  = 1.4
    # t1    = 0.83
    # t2    = 0.921
    # hight = 4.9
elif("Histogram-Frequency-based/output/" in path):
    title = "Histogram Frequency-based metric"
    name  = 'hf'
    # xmax  = .5
    # t1    = 0.259
    # t2    = 0.294
    # hight = 95
elif("FM/output/" in path):
    title = "Frequency Domain metric"
    name  = 'fm'
    # xmax  = .1
    # t1    = 0.392
    # t2    = 0.579
    # hight = 3.9
elif("cpbd/output/" in path):
    title = "CPBD metric"
    name  = 'cpbd'
    # xmax  = 1
    # t1    = 0.392
    # t2    = 0.579
    # hight = 3.9
elif('merge_metrics/cpbd_lv' in path):
    title = 'Merge of CPBD and Laplacian Variance'
    name  = 'cpbd_lv'
    # xmax  = 1.5
    # t1    = 0.63
    # t2    = 0.752
    # hight = 5.1
elif('merge_metrics/cpbd_HF/' in path):
    title = 'Merge of CPBD and Histogram Frequency-based'
    name  = 'cpbd_hf'
    # xmax  = .7
    # t1    = 0.335
    # t2    = 0.424
    # hight = 8
elif('merge_metrics/HF_lv' in path):
    title = 'Merge of Histogram Frequency-based and Laplacian Variance'
    name  = 'hf_lv'
    # xmax  = 1.5
    # t1    = 0.55
    # t2    = 0.599
    # hight = 7.1
elif('merge_metrics/cpbd_HF_lv' in path):
    title = 'Merge of CPBD, HF and Laplacian Variance'
    name  = 'cpbd_hf_lv'
#     xmax  = 2
#     t1    = 0.695
#     t2    = 0.767
#     hight = 5.8
# else:
#     title = "Merge"
#     name  = 'merge'


def open_data(filename):
    with open(path + filename, 'r') as file:
        data = file.read()
        data = [float(i) for i in data.split()]
    return data

def plot_density():
    plt.clf()
    n_bins = 20

    yblurry = list(filter(lambda x: x  < 1.4, blurry))
    (mu, sigma) = norm.fit(list(filter(lambda x: x  < 1.4, yblurry)))
    n, bins, patches = plt.hist(yblurry, bins=n_bins, density=True, alpha=0.6, stacked=True, color="blue", label="Hist of Blurry")
    plt.plot(bins, norm.pdf( bins, mu, sigma), '-', linewidth=2, color='orange', label='Norm. approx. of Blurry')
    ysharp=list(filter(lambda x: x  < 1.4, sharp))
    (mu, sigma) = norm.fit(ysharp)
    n, bins, patches = plt.hist(ysharp, bins=n_bins, density=True, alpha=0.6, stacked=True, color='green', label='Hist of No problems')
    plt.plot(bins, norm.pdf( bins, mu, sigma), '-', linewidth=2, color='red', label='Norm. approx. of No Problems')
    plt.xlabel('Metric score output')
    plt.ylabel('Density')
    # plt.xlim(right=xmax)
    # plt.vlines(t1, 0, hight, linestyles='--', colors='b', label="threshold: " + str(t1))
    # plt.vlines(t2, 0, hight, linestyles='-.', colors='b', label="threshold: " + str(t2))
    plt.title(title)
    plt.legend(loc="upper right")
    plt.savefig(path + 'output_dens_' + name + '.png')
    plt.savefig('results/density/' + 'output_dens_' + name + p_name + '.png')

def plot_conf(y_true, y_pred, threshold):
    plt.clf()
    conf_matrix = metrics.confusion_matrix(y_true, y_pred)
    disp = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['blur', 'sharp'])
    disp.plot()
#    plt.savefig(path + 'many_conf' + str(round(threshold, 3)) + '_output_conf_mat_' + name + '.png')
    plt.savefig(path + str(round(threshold, 3)) + '_output_conf_mat_' + name + '.png')
    plt.savefig('results/conf/' + 'output_conf_' + name + p_name + '.png')
    return conf_matrix.ravel()

def plot_roc(y_true, y_score):
    plt.clf()
    fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)
    roc_auc = metrics.auc(fpr, tpr)
    roc_display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc).plot()
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.savefig(path + 'output_roc_' + name + '.png')
    plt.savefig('results/roc/' + 'output_roc_' + name + p_name + '.png')
    return fpr, tpr, threshold

def print_acc_f1(y_true, y_score, y_pred):
    print("ACC             : " + str(round(metrics.accuracy_score(y_true, y_pred), 3))) # https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score
    print("F1-score        : " + str(round(metrics.f1_score(y_true, y_pred), 3))) # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score

def init_y():
    y_true = np.array([0]*len(blurry) + [1]*len(sharp)) # blur is negative, sharp is positive
    y_score = np.concatenate([blurry, sharp])
    return y_true, y_score

def plot_box(sharp, blurry, gauss2, gauss3, gauss4):
    plt.clf()
    if name == 'lv':
        sharp = [i for i in sharp if i < 2]
    plt.boxplot([sharp, blurry, gauss2, gauss3, gauss4], labels=['sharp', 'blurry', 'gauss2', 'gauss3', 'gauss4'])
    plt.title(title)
    plt.savefig(path + 'output_boxplot_' + name)
    plt.savefig('results/box/' + 'output_box_' + name + p_name + '.png')


blurry = open_data('out_blurry.txt')
blurry = blurry + open_data('out_synth_blurry.txt')
x1 = list(range(len(blurry)))
sharp = open_data('out_no_problems.txt')
sharp = sharp + open_data('out_synth_no_problems.txt')
x2 = list(range(len(sharp)))
gauss2 = open_data('out_synth_blurry_gaussian_2.0.txt')
gauss3 = open_data('out_synth_blurry_gaussian_3.0.txt')
gauss4 = open_data('out_synth_blurry_gaussian_4.0.txt')

plt.plot(x1, blurry, 'o-', label = 'Blurry')
plt.plot(x2, sharp, 'o-', label = 'No problems')
plt.title(title + ", avg. speed = " + avg_time + "s")
plt.xlabel("Image no.")
plt.ylabel("Score")
plt.grid(True)
plt.legend()
plt.savefig(path + 'output_basic_' + name + '.png')
# plt.savefig('results/basic/' + 'output_basic_' + name + p_name + '.png')

plot_density()
y_true, y_score = init_y()
fpr, tpr, threshold = plot_roc(y_true, y_score)
# fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)
plot_box(sharp, blurry, gauss2, gauss3, gauss4)

print(title)
for false_pos_rate, true_pos_rate, t in zip(fpr, tpr, threshold):
    plt.close('all')
    y_pred = list(map(lambda s: 0 if s < t else 1, blurry + sharp))
#    tn, fp, fn, tp = plot_conf(y_true, y_pred, t)
    tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()
    print("\n...... threshold: " + str(round(t, 3)))
    print("TPR, sensitivity: " + str(round(true_pos_rate, 3)))
    print("FPR             : " + str(round(false_pos_rate, 3)))
    print("TNR, specificity: " + str(round(tn/(tn+fp), 3)))
    if tp+fp:
        print("PPV, precision  : " + str(round(tp/(tp+fp), 3)))
    else:
        print("PPV, precision  : 1.0")
    print_acc_f1(y_true, y_score, y_pred)
