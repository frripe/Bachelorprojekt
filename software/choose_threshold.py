# python3 visualize_stats.py cpbd/output/
import re
import bisect
import metrics

def _extract_data(path):
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
        f1  = re.match('^F1-score        : (\d\.\d*)\n', line)
        if f1:
            F1.append(float(f1.group(1)))
    return threshold, TPR, FPR, TNR, PPV, ACC, F1

def _find_thresh_multiple(fpr):
    threshold, f1, metric = 0, 0, 0
    for index in range(0, len(metrics.metrics)):
        threshold_new, f1_new = _find_thresh(fpr, metrics.metrics[index])
        if f1_new > f1:
            threshold, f1 = threshold_new, f1_new
            metric = index
    return threshold, metric # metric index (int)

def _find_thresh(fpr, path):
    threshold, TPR, FPR, TNR, PPV, ACC, F1 = _extract_data(path)
    index_max = bisect.bisect_right(FPR, fpr)
    F1_slice = F1[0:index_max]
    F1_highest = max(F1_slice)
    threshold_index = F1_slice.index(F1_highest)
    return threshold[threshold_index], F1_highest

def find_threshold(fpr=0.1, quick=False):
    if quick:
        return _find_thresh(fpr, 'metrics_and_training_code/Histogram-Frequency-based/output/')[0], metrics.string_to_index('metrics_and_training_code/Histogram-Frequency-based/output/')
    return _find_thresh_multiple(fpr)
