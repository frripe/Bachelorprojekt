# python3 visualize_stats.py cpbd/output/
import sys
import re
import matplotlib.pyplot as plt

path = sys.argv[1]

if('laplacian_variance/output/' in path):
    title = "Laplacian Variance metric"
    name  = 'lv'
    xmax  = 2
    t1    = 0.83
    t2    = 0.921
    hight = 4.9
elif('Histogram-Frequency-based/output/' in path):
    title = "Histogram Frequency-based metric"
    name  = 'hf'
    xmax  = .5
    t1    = 0.259
    t2    = 0.294
    hight = 95
elif('cpbd/output/' in path):
    title = "CPBD metric"
    name  = 'cpbd'
    xmax  = 1
    t1     = 0.392
    t2     = 0.579
    hight = 3.9
elif('merge_metrics/cpbd_lv/' in path):
    title = 'Merge of CPBD and Laplacian Variance'
    name  = 'cpbd_lv'
    xmax  = 1.5
    t1    = 0.63
    t2    = 0.752
    hight = 5.1
elif('merge_metrics/cpbd_HF/' in path):
    title = 'Merge of CPBD and Histogram Frequency-based'
    name  = 'cpbd_hf'
    xmax  = .7
    t1    = 0.335
    t2    = 0.424
    hight = 8
elif('merge_metrics/HF_lv/' in path):
    title = 'Merge of Histogram Frequency-based and Laplacian Variance'
    name  = 'hf_lv'
    xmax  = 1.5
    t1    = 0.55
    t2    = 0.599
    hight = 7.1
elif('merge_metrics/cpbd_HF_lv/' in path):
    title = 'Merge of CPBD, HF and Laplacian Variance'
    name  = 'cpbd_hf_lv'
    xmax  = 2
    t1    = 0.695
    t2    = 0.767
    hight = 5.8
else:
    title = "Merge"
    name  = 'merge'

#...... threshold: 0.572
#TPR, sensitivity: 0.186
#FPR             : 0.048
#TNR, specificity: 0.952
#PPV, precision  : 0.738
#ACC: 0.6314878892733564
#F1-score: 0.297029702970297

threshold, TPR, FPR, TNR, PPV, ACC, F1 = [], [], [], [], [], [], []
#o=0
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

#print('\nthreshold ' + str(threshold))
#print('\nTPR ' + str(TPR))
#print('\nFPR ' + str(FPR))
#print('\nTNR ' + str(TNR))
#print('\nPPV ' + str(PPV))
#print('\nF1 ' + str(F1))
#print('\nACC ' + str(ACC))

plt.plot(threshold, TPR      , '-', label = 'TPR')
plt.plot(threshold, FPR      , '-', label = 'FPR')
plt.plot(threshold, TNR      , '-', label = 'TNR')
plt.plot(threshold, PPV      , '-', label = 'PPV')
plt.plot(threshold, ACC      , '-', label = 'ACC')
plt.plot(threshold, F1       , '-', label = 'F1-score')
# plt.vlines(t1, 0, 1, linestyles='--', colors='b', label="threshold: " + str(t1))
# plt.vlines(t2, 0, 1, linestyles='-.', colors='b', label="threshold: " + str(t2))

plt.xlim(min(threshold), xmax)
plt.title(title)
plt.xlabel("Threshold")
plt.ylabel("Value")
plt.grid(True)
plt.legend()
# plt.savefig('results/threshold/' + 'threshold_test_scores_' + name + '.png')
plt.savefig(path + 'threshold_test_scores_' + name + '.png')
