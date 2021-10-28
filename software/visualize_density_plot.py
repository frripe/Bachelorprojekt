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
no = sys.argv[2]

print(path)

if(path == "laplacian_variance/output/"):
    title = "Laplacian Variance metric"
#    threshold = 0.861
elif(path == "FM/output/"):
    title = "Frequency Domain metric"
#    threshold = 0.235
elif(path == "Histogram-Frequency-based/output/"):
    title = "Histogram Frequency-based metric"
#    threshold = 0.454
elif(path == "cpbd/output/"):
    title = "CPBD metric"
#    threshold = 0.375
elif(path == 'merge_metrics/cpbd_lv/'):
    title = 'Merge of CPBD and Laplacian Variance'
#    threshold = 0.5
else:
    title = "Merge"
#    threshold = 0.5

def open_data(filename):
    with open(path + filename, 'r') as file:
        data = file.read()
        data = [float(i) for i in data.split()]
    return data

def plot_density(blur, shar, with_gauss):
    plt.clf()
    n_bins = 20
    (mu, sigma) = norm.fit(blur)
    n, bins, patches = plt.hist(blur, bins=n_bins, density=True, alpha=0.6, stacked=True, color="blue", label="Hist of Blurry")
    plt.plot(bins, norm.pdf( bins, mu, sigma), '-', linewidth=2, color='orange', label='Norm. approx. of Blurry')
    (mu, sigma) = norm.fit(shar)
    n, bins, patches = plt.hist(shar, bins=n_bins, density=True, alpha=0.6, stacked=True, color='green', label='Hist of No problems')
    plt.plot(bins, norm.pdf( bins, mu, sigma), '-', linewidth=2, color='red', label='Norm. approx. of No Problems')
    plt.xlabel('Metric score output')
    plt.ylabel('Density')
    plt.title(title)
    plt.legend(loc="upper right")
    plt.savefig(path + with_gauss + '/many_dens/' + str(no) + '_output_dens.png')
    # plt.savefig(path + 'output_dens.png')

def plot_roc(y_true, y_score, with_gauss):
    fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)
    # print(threshold)
    roc_auc = metrics.auc(fpr, tpr)
    print(with_gauss + "                       roc_auc: " + str(roc_auc))
    roc_display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc).plot()
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.savefig(path + with_gauss + '/many_roc/' + str(no) + '_output_roc.png')

def plot_box(sharp, blurry, gauss2, gauss3, gauss4):
    plt.clf()
    plt.boxplot([sharp, blurry, gauss2, gauss3, gauss4], labels=['sharp', 'blurry', 'gauss2', 'gauss3', 'gauss4'])
    plt.title(title)
    plt.savefig(path + 'many_gauss/many_box/' + str(no) + '_output_box.png')

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
plt.title(title)
plt.xlabel("Image no.")
plt.ylabel("Score")
plt.grid(True)
plt.legend()
plt.savefig(path + 'many_no_gauss/many_basic/' + str(no) + '_output_basic.png')
# plt.savefig(path + 'output_basic.png')

plot_box(sharp, blurry, gauss2, gauss3, gauss4)
plot_density(blurry, sharp, 'many_no_gauss')
plot_density(blurry + gauss2 + gauss3 + gauss4, sharp, 'many_gauss')
y_true = np.array([0]*len(blurry) + [1]*len(sharp))
y_score = np.concatenate([blurry, sharp])
plot_roc(y_true, y_score, 'many_no_gauss')
y_true = np.array([0]*len(blurry) + [1]*len(sharp) + [0]*len(gauss2) + [0]*len(gauss3) + [0]*len(gauss4))
y_score = np.concatenate([blurry, sharp, gauss2, gauss3, gauss4])
plot_roc(y_true, y_score, 'many_gauss')
