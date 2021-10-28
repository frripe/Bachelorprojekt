# python3 visualize_stats.py cpbd/output/
import re
import sys
import matplotlib.pyplot as plt

path = str(sys.argv[1])

if('laplacian_variance/output/' in path):
    title = "Laplacian Variance metric"
    name  = 'lv'
elif('Histogram-Frequency-based/output/' in path):
    title = "Histogram Frequency-based metric"
    name  = 'hf'
elif('cpbd/output/' in path):
    title = "CPBD metric"
    name  = 'cpbd'
elif('merge_metrics/cpbd_lv' in path):
    title = 'Merge of CPBD and Laplacian Variance'
    name  = 'cpbd_lv'
elif('merge_metrics/cpbd_HF/' in path):
    title = 'Merge of CPBD and Histogram Frequency-based'
    name  = 'cpbd_hf'
elif('merge_metrics/HF_lv' in path):
    title = 'Merge of Histogram Frequency-based and Laplacian Variance'
    name  = 'hf_lv'
elif('cpbd_HF_lv' in path):
    title = 'Merge of CPBD, HF and Laplacian Variance'
    name  = 'cpbd_hf_lv'

threshold, TPR, FPR, TNR, PPV, ACC, F1 = [], [], [], [], [], [], []
for line in open(path + 'results.txt'):
    t = re.match('^...... threshold: (\d\.\d*)\n', line)
    if t:
        threshold.append(float(t.group(1)))

    tpr = re.match('^TPR, sensitivity: (\d\.\d*)\n', line)
    if tpr:
        TPR.append(float(tpr.group(1)))

    fpr = re.match('^FPR             : (\d\.\d*)\n', line)
    if fpr:
        FPR.append(float(fpr.group(1)))

    tnr = re.match('^TNR, specificity: (\d\.\d*)\n', line)
    if tnr:
        TNR.append(float(tnr.group(1)))

    ppv = re.match('^PPV, precision  : (\d\.\d*)\n', line)
    if ppv:
        PPV.append(float(ppv.group(1)))
    ppv = re.match('^PPV, precision  : nan\n', line)
    if ppv:
        PPV.append(1)

    acc = re.match('^ACC             : (\d\.\d*)\n', line)
    if acc:
        ACC.append(float(acc.group(1)))

    f1 = re.match('^F1-score        : (\d\.\d*)\n', line)
    if f1:
        F1.append(float(f1.group(1)))

plt.plot(threshold, TPR, '-', label = 'TPR')
plt.plot(threshold, FPR, '-', label = 'FPR')
plt.plot(threshold, TNR, '-', label = 'TNR')
plt.plot(threshold, PPV, '-', label = 'PPV')
plt.plot(threshold, ACC, '-', label = 'ACC')
plt.plot(threshold, F1 , '-', label = 'F1-score')

plt.title(title)
plt.xlabel("Threshold")
plt.ylabel("Value")
plt.grid(True)
plt.legend()
plt.savefig('results/threshold/' + 'threshold_test_scores_' + name + '_' + path.replace('/', '-') + '.png')
plt.savefig(path + 'threshold_test_scores_' + name + '.png')
