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

with open(path + 'time.txt') as f:
    times = [float(t) for t in f]
    f.close()
avg_time = str(round(sum(times)/len(times), 4))

if(path == "laplacian_variance/output/"):
    title = "Laplacian Variance metric"
    threshold = 0.861
elif(path == "FM/output/"):
    title = "Frequency Domain metric"
    threshold = 0.235
elif(path == "Histogram-Frequency-based/output/"):
    title = "Histogram Frequency-based metric"
    threshold = 0.454
elif(path == "cpbd/output/"):
    title = "CPBD metric"
    threshold = 0.375
elif(path == 'merge_metrics/cpbd_lv/'):
    title = 'Merge of CPBD and Laplacian Variance'
    threshold = 0.5
else:
    title = "Merge"
    threshold = 0.5


y1=[]
with open(path + 'out_blurry.txt', 'r') as file:
    y1 = file.read()
    y1 = [float(i) for i in y1.split()]
with open(path + 'out_synth_blurry.txt', 'r') as file:
    f = file.read()
    f = [float(i) for i in f.split()]
y1 = y1 + f
x1 = list(range(len(y1)))
#m1 = np.mean(y1)
#y3 = [m1]*47

y2=[]
with open(path + 'out_no_problems.txt', 'r') as file:
    y2 = file.read()
    y2 = [float(i) for i in y2.split()]
with open(path + 'out_synth_no_problems.txt', 'r') as file:
    f = file.read()
    f = [float(i) for i in f.split()]
y2 = y2 + f
x2 = list(range(len(y2)))
#m2 = np.mean(y2)
#y4 = [m2]*47

#x0 = list(range(1, 252))
#y0 = []
#with open('laplacian_variance/output/out_synth_blur.txt', 'r') as file:
#    y0 = file.read()
#    y0 = [float(i) for i in y0.split()]
#
#
#print('LV mean = ' + str(round( min(m1, m2) + abs((m2-m1)/2), 3)))
#
#plt.ylim([0, 1])
plt.plot(x1,y1, 'o-', label = 'Blurry')
plt.plot(x2,y2, 'o-', label = 'No problems')
#plt.plot(x0,y0, 'o-', label = 'Synth blurry')
#plt.plot(x1,y3, '-', label = 'Mean of blurry')
#plt.plot(x1,y4, '-', label = 'Mean of no problems')
plt.title(title + ", avg. speed = " + avg_time + "s")
plt.xlabel("Image no.") 
plt.ylabel("Score")
plt.grid(True)
plt.legend()
plt.savefig(path + 'output_basic.png')


def plot_density():
    plt.clf()
    n_bins = 20
    (mu, sigma) = norm.fit(y1)
    n, bins, patches = plt.hist(y1, bins=n_bins, density=True, alpha=0.6, stacked=True, color="blue", label="Hist of Blurry")
    plt.plot(bins, norm.pdf( bins, mu, sigma), '-', linewidth=2, color='orange', label='Norm. approx. of Blurry')
    (mu, sigma) = norm.fit(y2)
    n, bins, patches = plt.hist(y2, bins=n_bins, density=True, alpha=0.6, stacked=True, color='green', label='Hist of No problems')
    plt.plot(bins, norm.pdf( bins, mu, sigma), '-', linewidth=2, color='red', label='Norm. approx. of No Problems')
    plt.xlabel('Metric score output')
    plt.ylabel('Density')
    plt.title(title)
    plt.legend(loc="upper right")
#    plt.show()
    plt.savefig(path + 'output_dens.png')


#def plot_density():
#    plt.clf()
#    y1.sort()
#    y2.sort()
#    yy = [[i] for i in y1]
#    yy2 = [[i] for i in y2]
#    kde = KernelDensity(kernel='gaussian', bandwidth=1).fit(yy)
#    plt.plot(y1, kde.score_samples(yy), 'o-', label = 'Blurry')
#    kde = KernelDensity(kernel='gaussian', bandwidth=1).fit(yy2)
#    plt.plot(y2, kde.score_samples(yy2), 'o-', label = 'No problems')
#    plt.title(title)
#    plt.xlabel("Score") 
#    plt.ylabel("Density of observations")
#    plt.grid(True)
#    plt.legend()
#    plt.show()
#    plt.savefig(path + 'output_density.png')
#

def plot_conf(tb, fb, ts, fs, threshold):
    conf_matrix = np.array([[ts, fb], [fs, tb]])
    disp = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['sharp', 'blur'])
    plt.title(title)
    plt.legend()
    disp.plot()
    plt.savefig(path + str(threshold) + '_output_conf_mat.png')

def plot_roc(y_true, y_score):
    fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)
    #print(threshold)
    roc_auc = metrics.auc(fpr, tpr)
    roc_display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc).plot()
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.savefig(path + 'output_roc.png')
    return fpr, tpr, threshold

def print_acc_f1(y_true, y_score, threshold):
    a = np.where(y_score > threshold, 1, 0)
    print("\n" + title)
    print("ACC = " + str(metrics.accuracy_score(y_true, a))) # https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score
    print("F1-score = " + str(metrics.f1_score(y_true, a))) # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score

def init_y():
    y_true = np.array([0]*len(y1) + [1]*len(y2))
    y_score = np.concatenate([y1, y2])
    return y_true, y_score

def init_binary(threshold):
    tb, fb, ts, fs = 0,0,0,0 # blur is negative, sharp is positive
    for i in y1: # blur
        if i <= threshold:
            tb+=1
        else:
            fs+=1
    for i in y2: # sharp
        if i <= threshold:
            fb+=1
        else:
            ts+=1
    return tb, fb, ts, fs

plot_density()
y_true, y_score = init_y()
fpr, tpr, threshold = plot_roc(y_true, y_score)

for t in threshold:
    plt.clf()
    print("threshold: " + str(t))
    tb, fb, ts, fs = init_binary(t)
    plot_conf(tb, fb, ts, fs, t)
    print_acc_f1(y_true, y_score, t)

