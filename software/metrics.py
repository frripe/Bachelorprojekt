metrics = [
    'metrics_and_training_code/laplacian_variance/output/jpg/',
    'metrics_and_training_code/Histogram-Frequency-based/output/',
    'metrics_and_training_code/cpbd/output/',
    'metrics_and_training_code/merge_metrics/cpbd_lv_jpg/many_alpha/alpha_4/',
    'metrics_and_training_code/merge_metrics/cpbd_HF/many_alpha/alpha_2/',
    'metrics_and_training_code/merge_metrics/HF_lv_jpg/many_alpha/alpha_7/',
    'metrics_and_training_code/merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_2_6/',
]

i2s = dict(list(enumerate(metrics)))

def index_to_string(metric_index):
    return i2s[metric_index]

def string_to_index(metric_string):
    return metrics.index(metric_string)
