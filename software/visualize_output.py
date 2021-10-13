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
elif(path == 'merge_metrics/cpbd_HF/'):
    title = 'Merge of CPBD and Histogram Frequency-based'
#    threshold = 0.5
elif(path == 'merge_metrics/HF_lv/'):
    title = 'Merge of Histogram Frequency-based and Laplacian Variance'
#    threshold = 0.5
elif(path == 'merge_metrics/cpbd_HF_lv/'):
    title = 'Merge of CPBD, HF and Laplacian Variance'
#    threshold = 0.5
else:
    title = "Merge"
#    threshold = 0.5


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

def plot_conf(y_true, y_pred, threshold):
    conf_matrix = metrics.confusion_matrix(y_true, y_pred)#np.array([[ts, fb], [fs, tb]])
#    tn, fp, fn, tp = conf_matrix.ravel()
    disp = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['blur', 'sharp'])
#    plt.title(title)
#    plt.legend()
    disp.plot()
#    plt.show()
    plt.savefig(path + str(round(threshold, 3)) + '_output_conf_mat.png')
    return conf_matrix.ravel()

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

def print_acc_f1(y_true, y_score, y_pred): #, threshold):
#    a = np.where(y_score > threshold, 1, 0)
    print("ACC: " + str(metrics.accuracy_score(y_true, y_pred))) # https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score
    print("F1-score: " + str(metrics.f1_score(y_true, y_pred))) # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score

def init_y():
    y_true = np.array([0]*len(y1) + [1]*len(y2)) # blur is negative, sharp is positive
    y_score = np.concatenate([y1, y2])
    return y_true, y_score

#def init_binary(threshold):
#    tp, fp, tn, fn = 0,0,0,0 # blur is negative, sharp is positive
#    for i in y1: # blur
#        if i < threshold:
#            tn+=1
#        else:
#            fp+=1
#    for i in y2: # sharp
#        if i < threshold:
#            fn+=1
#        else:
#            tp+=1
#    return tp, fp, tn, fn

plot_density()
y_true, y_score = init_y()
fpr, tpr, threshold = plot_roc(y_true, y_score)
#fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)
#y_pred = list(map(lambda s: 0 if s < threshold[3] else 1, y1 + y2))
#print("y_true: " + str(y_true) + "\ny_score: " + str(y_score) + "\ny_pred: " + str(y_pred))
#print("confusion_matrix(y_true, y_pred): " + str(metrics.confusion_matrix(y_true, y_pred)))
#
#tp, fp, tn, fn = init_binary(threshold[10])
#print("threshold: " + str(threshold[3]) + str(threshold))

#print('tp ' + str(tp) + ' fp ' + str(fp) + ' tn ' + str(tn) + ' fn ' + str(fn))
#print('tpr ' + str(tpr) + '\nfpr ' + str(fpr))
#print('tpr2 ' + str(tp/(tp+fn)) + ' fpr2 ' + str(fp/(fp+tn)))
#plot_conf(tp, fp, tn, fn, threshold[3])
#tp, fp, tn, fn = init_binary(threshold[3])
#print('tp ' + str(tp) + ' fp ' + str(fp) + ' tn ' + str(tn) + ' fn ' + str(fn))
#print('tpr2 ' + str(tp/(tp+fn)) + ' fpr2 ' + str(fp/(fp+tn)))

print("\n" + title)
for false_pos_rate, true_pos_rate, t in zip(fpr, tpr, threshold):
    plt.close('all')
#tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()

#    tp, fp, tn, fn = init_binary(t)
    y_pred = list(map(lambda s: 0 if s < t else 1, y1 + y2))
    tn, fp, fn, tp = plot_conf(y_true, y_pred, t)
    print("\n...... threshold: " + str(round(t, 3)))
    print("TPR, sensitivity: " + str(round(true_pos_rate, 3)))
    print("FPR             : " + str(round(false_pos_rate, 3)))
    print("TNR, specificity: " + str(round(tn/(tn+fp), 3)))
    print("PPV, precision  : " + str(round(tp/(tp+fp), 3)))
    print_acc_f1(y_true, y_score, y_pred)#, t)

