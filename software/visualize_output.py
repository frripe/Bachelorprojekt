import os
import cpbd
import imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics

# folder with the images in the filesystem
#path = str(input()).rstrip()

# amount of images in the folder
#n = len(os.listdir(path))

with open('cpbd/output/time.txt') as f:
    times = [float(t) for t in f]
    f.close()
avg_time = str(sum(times)/len(times))

#for i in range(1, n + 1):
#    time_start = time.time()
#    input_image = imageio.imread(path + str(i) + '.bmp', pilmode='L')
#    print(cpbd.compute(input_image))
#    time_end = time.time()
#    file_object.write(str(time_end - time_start)) # added # measured in seconds
#
# python3 laplacian_variance/output/visualize_output.py
#
#y1=[]
#with open('laplacian_variance/output/out_blur.txt', 'r') as file:
#    y1 = file.read()
#    y1 = [float(i) for i in y1.split()]
#x1 = list(range(len(y1)))
#m1 = np.mean(y1)
#y3 = [m1]*47
#
#y2=[]
#with open('laplacian_variance/output/out_no_problems.txt', 'r') as file:
#    y2 = file.read()
#    y2 = [float(i) for i in y2.split()]
#
#x2 = list(range(len(y2)))
#m2 = np.mean(y2)
#y4 = [m2]*47
#
#x0 = list(range(1, 252))
#y0 = []
#with open('laplacian_variance/output/out_synth_blur.txt', 'r') as file:
#    y0 = file.read()
#    y0 = [float(i) for i in y0.split()]
#
#
#print('LV mean = ' + str(round( min(m1, m2) + abs((m2-m1)/2), 3)))
#
#plt.ylim([0.4, 1.4])
#plt.plot(x1,y1, 'o-', label = 'Blurry')
#plt.plot(x2,y2, 'o-', label = 'No problems')
#plt.plot(x0,y0, 'o-', label = 'Synth blurry')
#plt.plot(x1,y3, '-', label = 'Mean of blurry')
#plt.plot(x1,y4, '-', label = 'Mean of no problems')
#plt.title("Laplacian Variance metric, avg. speed = ???s") 
#plt.xlabel("Image no.") 
#plt.ylabel("Score")
#plt.grid(True)
#plt.legend()
#plt.savefig('laplacian_variance/output/output_laplacian_variance.png')
#
#
#tb, fb, ts, fs = 0,0,0,0 # blur is negative, sharp is positive
#y_true = np.array([0]*47 + [1]*34)
#y_score = np.array([])
#threshold = 0.861
#for i in y1: # blur
#    if i <= threshold:
#        tb+=1
#        y_score = np.append(y_score, [i])
#    else:
#        fs+=1
#        y_score = np.append(y_score, [i])
#for i in y2: # sharp
#    if i <= threshold:
#        fb+=1
#        y_score = np.append(y_score, [i])
#    else:
#        ts+=1
#        y_score = np.append(y_score, [i])
#print('tb: ' + str(tb))
#print('fb: ' + str(fb))
#print('ts: ' + str(ts))
#print('fs: ' + str(fs))
#conf_matrix = np.array([[ts, fb], [fs, tb]])
#disp = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['sharp', 'blur'])
#plt.title('Laplacian Variance metric')
#plt.legend()
#disp.plot()
#plt.savefig('laplacian_variance/output/output_laplacian_variance_conf_mat.png')
#
#fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)
#print(threshold)
#roc_auc = metrics.auc(fpr, tpr)
#roc_display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc).plot()
#plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
#plt.xlabel('False Positive Rate')
#plt.ylabel('True Positive Rate')
#plt.title('Laplacian Variance metric')
#plt.legend(loc="lower right")
#plt.savefig('laplacian_variance/output/output_laplacian_variance_roc.png')
#
