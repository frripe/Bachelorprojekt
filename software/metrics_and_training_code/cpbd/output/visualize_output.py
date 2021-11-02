# python3 cpbd/output/visualize_output.py
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics

x1 = list(range(1, 48))
y1 = []
with open('cpbd/output/out_blur.txt', 'r') as file:
    y1 = file.read()
    y1 = [float(i) for i in y1.split()]
m1 = np.mean(y1)
y3 = [m1]*47

x2 = list(range(1, 35))
y2 = []
with open('cpbd/output/out_no_problems.txt', 'r') as file:
    y2 = file.read()
    y2 = [float(i) for i in y2.split()]
m2 = np.mean(y2)
y4 = [m2]*47

x0 = list(range(1, 252))
y0 = []
with open('cpbd/output/out_synth_blur.txt', 'r') as file:
    y0 = file.read()
    y0 = [float(i) for i in y0.split()]

print('CPBD mean = ' + str(round( min(m1, m2) + abs((m2-m1)/2), 3)))

plt.ylim([0, 1])
plt.plot(x1,y1, 'o-', label = 'Blurry')
plt.plot(x2,y2, 'o-', label = 'No problems')
plt.plot(x0,y0, 'o-', label = 'Synthetic blur')
plt.plot(x1,y3, '-', label = 'Mean of blurry')
plt.plot(x1,y4, '-', label = 'Mean of no problems')
plt.title("CPBD, avg. speed = 1.042s") 
plt.xlabel("Image no.") 
plt.ylabel("Score")
plt.grid(True)
plt.legend()
plt.savefig('cpbd/output/output_cpbd.png')


tb, fb, ts, fs = 0,0,0,0 # blur is negative, sharp is positive
y_true = np.array([0]*47 + [1]*34)
y_score = np.array([])
threshold = 0.375
for i in y1: # blur
    if i <= threshold:
        tb+=1
        y_score = np.append(y_score, [i])
    else:
        fs+=1
        y_score = np.append(y_score, [i])
for i in y2: # sharp
    if i <= threshold:
        fb+=1
        y_score = np.append(y_score, [i])
    else:
        ts+=1
        y_score = np.append(y_score, [i])
#print('tb: ' + str(tb))
#print('fb: ' + str(fb))
#print('ts: ' + str(ts))
#print('fs: ' + str(fs))
conf_matrix = np.array([[ts, fb], [fs, tb]])
disp = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['sharp', 'blur'])
plt.title('CPBD')
plt.legend()
disp.plot()
plt.savefig('cpbd/output/output_cpbd_conf_mat.png')

fpr, tpr, _ = metrics.roc_curve(y_true, y_score)
roc_auc = metrics.auc(fpr, tpr)
roc_display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc).plot()
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('CPBD')
plt.legend(loc="lower right")
plt.savefig('cpbd/output/output_cpbd_roc.png')

