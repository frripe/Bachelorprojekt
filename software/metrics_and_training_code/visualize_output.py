# python3 visualize_output.py cpbd/output/
import os
import sys
import imageio
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
from scipy.stats import norm


def open_data(path, filename):
    with open(path + filename, 'r') as file:
        data = file.read()
        data = [float(i) for i in data.split()]
    return data

def plot_density(path, title, name):
    plt.clf()
    n_bins = 20

    # yblurry = list(filter(lambda x: x < 1.4, blurry))
    (mu, sigma) = norm.fit(blurry)
    n, bins, patches = plt.hist(blurry, bins=n_bins, density=True, alpha=0.6, stacked=True, color="blue", label="Hist of Blurry")
    plt.plot(bins, norm.pdf( bins, mu, sigma), '-', linewidth=2, color='orange', label='Norm. approx. of Blurry')
    # ysharp=list(filter(lambda x: x  < 1.4, sharp))
    (mu, sigma) = norm.fit(sharp)
    n, bins, patches = plt.hist(sharp, bins=n_bins, density=True, alpha=0.6, stacked=True, color='green', label='Hist of No problems')
    plt.plot(bins, norm.pdf( bins, mu, sigma), '-', linewidth=2, color='red', label='Norm. approx. of No Problems')
    plt.xlabel('Metric score output')
    plt.ylabel('Density')
    plt.title(title)
    plt.legend(loc="upper right")
    plt.savefig(path + 'output_dens_' + name + '.png')
    plt.savefig('results/density/' + name + '/output_dens_' + name + p_name + '.png')

def plot_conf(y_true, y_pred, threshold):
    conf_matrix = metrics.confusion_matrix(y_true, y_pred)
    disp = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['blur', 'sharp'])
    disp.plot()
    plt.show()
    plt.close()
# #    plt.savefig(path + 'many_conf' + str(round(threshold, 3)) + '_output_conf_mat_' + name + '.png')
#     plt.savefig(path + str(round(threshold, 3)) + '_output_conf_mat_' + name + '.png')
#     plt.savefig('results/conf/' + name + '/output_conf_' + name + p_name + '.png')
    return conf_matrix.ravel()

def plot_roc(path, title, name, y_true, y_score):
    plt.clf()
    fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)
    roc_auc = metrics.auc(fpr, tpr)
    print("AUC             : " + str(roc_auc))
    roc_display = metrics.RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc).plot()
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.savefig(path + 'output_roc_' + name + '.png')
    plt.savefig('results/roc/' + name + '/output_roc_' + name + p_name + '.png')
    return fpr, tpr, threshold

def plot_box(path, title, name, sharp, blurry, gauss2, gauss3, gauss4, save=1):
    plt.clf()
    plt.boxplot([sharp, blurry, gauss2, gauss3, gauss4], labels=['sharp', 'blurry', 'gauss2', 'gauss3', 'gauss4'])
    plt.title(title)
    if save:
        plt.savefig(path + 'output_boxplot_' + name)
        plt.savefig('results/box/' + name + '/output_box_' + name + p_name + '.png')
    else:
        plt.show()
        plt.close()

def init_y(blurry, sharp):
    y_true = np.array([0]*len(blurry) + [1]*len(sharp)) # blur is negative, sharp is positive
    y_score = np.concatenate([blurry, sharp])
    return y_true, y_score

def y_predicted(threshold, blurry, sharp):
    return list(map(lambda s: 0 if s < threshold else 1, blurry + sharp))

def print_acc_f1(y_true, y_score, y_pred):
    print("ACC             : " + str(metrics.accuracy_score(y_true, y_pred))) # https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score
    print("F1-score        : " + str(metrics.f1_score(y_true, y_pred))) # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score


def main():
    pass

if __name__ == "__main__":
    # folder with outputs
    path = str(sys.argv[1])
    p_name = '_' + path.replace('/', '-')

    if os.path.isfile(path + 'time.txt'):
        with open(path + 'time.txt') as f:
            times = [float(t) for t in f]
            f.close()
        avg_time = sum(times)/len(times)
        print("time            : " + str(avg_time))

    if("laplacian_variance/output/" in path):
        title = "Laplacian Variance metric"
        name  = 'lv'
    elif("Histogram-Frequency-based/output/" in path):
        title = "Histogram Frequency-based metric"
        name  = 'hf'
    elif("FM/output/" in path):
        title = "Frequency Domain metric"
        name  = 'fm'
    elif("cpbd/output/" in path):
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

    print(title)

    blurry = open_data(path, 'out_blurry.txt')
    blurry = blurry + open_data(path, 'out_synth_blurry.txt')
    x1 = list(range(len(blurry)))
    sharp = open_data(path, 'out_no_problems.txt')
    sharp = sharp + open_data(path, 'out_synth_no_problems.txt')
    x2 = list(range(len(sharp)))
    gauss2 = open_data(path, 'out_synth_blurry_gaussian_2.0.txt')
    gauss3 = open_data(path, 'out_synth_blurry_gaussian_3.0.txt')
    gauss4 = open_data(path, 'out_synth_blurry_gaussian_4.0.txt')

    plt.plot(x1, blurry, 'o-', label = 'Blurry')
    plt.plot(x2, sharp, 'o-', label = 'No problems')
    plt.title(title + ", avg. speed = " + str(round(avg_time, 4)) + "s")
    plt.xlabel("Image no.")
    plt.ylabel("Score")
    plt.grid(True)
    plt.legend()
    plt.savefig(path + 'output_basic_' + name + '.png')
    # plt.savefig('results/basic/' + 'output_basic_' + name + p_name + '.png')

    plot_density(path, title, name)
    y_true, y_score = init_y(blurry, sharp)
    fpr, tpr, threshold = plot_roc(path, title, name, y_true, y_score)
    # fpr, tpr, threshold = metrics.roc_curve(y_true, y_score)
    plot_box(path, title, name, sharp, blurry, gauss2, gauss3, gauss4)

    for false_pos_rate, true_pos_rate, t in zip(fpr, tpr, threshold):
        plt.close('all')
        y_pred = y_predicted(t, blurry, sharp)
    #    tn, fp, fn, tp = plot_conf(y_true, y_pred, t)
        tn, fp, fn, tp = metrics.confusion_matrix(y_true, y_pred).ravel()
        print("\n...... threshold: " + str(t))
        print("TPR, sensitivity: " + str(true_pos_rate))
        print("FPR             : " + str(false_pos_rate))
        print("TNR, specificity: " + str(tn/(tn+fp)))
        if tp+fp:
            print("PPV, precision  : " + str(tp/(tp+fp)))
        else:
            print("PPV, precision  : 1.0")
        print_acc_f1(y_true, y_score, y_pred)

main()
