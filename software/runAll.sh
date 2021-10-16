# chmod +x runAll.sh
# ./runAll.sh

# ./runFM.sh
# ./runHF.sh
# ./runLV.sh
# ./runCPBD.sh
#
#
# python3 visualize_output.py Histogram-Frequency-based/output/ > Histogram-Frequency-based/output/results.txt
# python3 visualize_output.py laplacian_variance/output/        > laplacian_variance/output/results.txt
# python3 visualize_output.py cpbd/output/                      > cpbd/output/results.txt

# python3 visualize_stats.py Histogram-Frequency-based/output/
# python3 visualize_stats.py laplacian_variance/output/
# python3 visualize_stats.py cpbd/output/

for alpha in {1..9}; do
    # rm -r merge_metrics/cpbd_lv/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/cpbd_lv/many_alpha/alpha_${alpha}/
    # python3 merge_metrics/merge_data.py cpbd/output/ laplacian_variance/output/ merge_metrics/cpbd_lv/many_alpha/alpha_${alpha}/ ${alpha}

    # rm -r merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/
    # python3 merge_metrics/merge_data.py cpbd/output/ Histogram-Frequency-based/output/ merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/ ${alpha}

    # rm -r merge_metrics/HF_lv/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/HF_lv/many_alpha/alpha_${alpha}/
    # python3 merge_metrics/merge_data.py Histogram-Frequency-based/output/ laplacian_variance/output/ merge_metrics/HF_lv/many_alpha/alpha_${alpha}/ ${alpha}

    rm -r merge_metrics/cpbd_HF_lv/many_alpha/alpha_${alpha}/
    mkdir -p merge_metrics/cpbd_HF_lv/many_alpha/alpha_${alpha}/
    # python3 merge_metrics/merge_data.py merge_metrics/HF_lv/ laplacian_variance/output/ merge_metrics/cpbd_HF_lv/many_alpha/alpha_${alpha}/ ${alpha}
    python3 merge_metrics/merge_data.py merge_metrics/cpbd_HF/many_alpha/alpha_1/ laplacian_variance/output/ merge_metrics/cpbd_HF_lv/many_alpha/alpha_${alpha}/ ${alpha}

    # python3 visualize_output.py merge_metrics/cpbd_lv/many_alpha/alpha_${alpha}/        > merge_metrics/cpbd_lv/many_alpha/alpha_${alpha}/results.txt
    # python3 visualize_output.py merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/        > merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/results.txt
    # python3 visualize_output.py merge_metrics/HF_lv/many_alpha/alpha_${alpha}/          > merge_metrics/HF_lv/many_alpha/alpha_${alpha}/results.txt
    python3 visualize_output.py merge_metrics/cpbd_HF_lv/many_alpha/alpha_${alpha}/     > merge_metrics/cpbd_HF_lv/many_alpha/alpha_${alpha}/results.txt

    # python3 visualize_stats.py merge_metrics/cpbd_lv/many_alpha/alpha_${alpha}/
    # python3 visualize_stats.py merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/
    # python3 visualize_stats.py merge_metrics/HF_lv/many_alpha/alpha_${alpha}/
    python3 visualize_stats.py merge_metrics/cpbd_HF_lv/many_alpha/alpha_${alpha}/
done
