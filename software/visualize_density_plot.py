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


y1=[]
with open(path + 'out_blurry.txt', 'r') as file:
    y1 = file.read()
    y1 = [float(i) for i in y1.split()]
with open(path + 'out_synth_blurry.txt', 'r') as file:
    f = file.read()
    f = [float(i) for i in f.split()]
y1 = y1 + f
x1 = list(range(len(y1)))

y2=[]
with open(path + 'out_no_problems.txt', 'r') as file:
    y2 = file.read()
    y2 = [float(i) for i in y2.split()]
with open(path + 'out_synth_no_problems.txt', 'r') as file:
    f = file.read()
    f = [float(i) for i in f.split()]
y2 = y2 + f
x2 = list(range(len(y2)))

plt.plot(x1,y1, 'o-', label = 'Blurry')
plt.plot(x2,y2, 'o-', label = 'No problems')
plt.title(title)
plt.xlabel("Image no.") 
plt.ylabel("Score")
plt.grid(True)
plt.legend()
#plt.savefig(path + 'many_basic/' + str(no) + '_output_basic.png')
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
#    plt.savefig(path + 'many_dens/' + str(no) + '_output_dens.png')
    plt.savefig(path + 'output_dens.png')

def plot_roc(y_true, y_score):
    fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)
    #print(threshold)
    roc_auc = metrics.auc(fpr, tpr)
    print("                                 roc_auc: " + str(roc_auc))
    roc_display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc).plot()
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
#    plt.savefig(path + 'many_roc/' + str(no) + '_output_roc.png')
    plt.savefig(path + 'output_roc.png')


plot_density()
y_true = np.array([0]*len(y1) + [1]*len(y2))
y_score = np.concatenate([y1, y2])
plot_roc(y_true, y_score)

