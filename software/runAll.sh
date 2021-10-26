# chmod +x runAll.sh
# ./runAll.sh

# echo "generating synthetic dataset..."
# python3 ../dataset/original/gen_synth.py
# echo "sharing jpg images with png and bmp..."
# python3 ../dataset/original/share_dataset.py
# echo "generating training and test datasets..."
# python3 ../dataset/gen_training_and_test_set.py 0.1

echo "running FM on full dataset..."
./runFM.sh    # png
# echo "running HF on full dataset..."
# ./runHF.sh    # jpg
echo "running LV on full dataset..."
./runLV.sh    # png, jpg?
echo "running CPBD on full dataset..."
./runCPBD.sh  # bmp

echo "visualizing output of FM..."
python3 visualize_output.py FM/output/                        > FM/output/results.txt
# echo "visualizing output of HF..."
# python3 visualize_output.py Histogram-Frequency-based/output/ > Histogram-Frequency-based/output/results.txt
echo "visualizing output of LV png..."
python3 visualize_output.py laplacian_variance/output/png/    > laplacian_variance/output/png/results.txt
echo "visualizing output of LV jpg..."
python3 visualize_output.py laplacian_variance/output/jpg/    > laplacian_variance/output/jpg/results.txt
echo "visualizing output of CPBD..."
python3 visualize_output.py cpbd/output/                      > cpbd/output/results.txt

# echo "visualizing statistics of HF..."
# python3 visualize_stats.py Histogram-Frequency-based/output/
echo "visualizing statistics of LV png..."
python3 visualize_stats.py laplacian_variance/output/png/
echo "visualizing statistics of LV jpg..."
python3 visualize_stats.py laplacian_variance/output/jpg/
echo "visualizing statistics of CPBD..."
python3 visualize_stats.py cpbd/output/

# echo "testing alpha-values for combined metrics..."
# for alpha in {1..9}; do
    # rm -r merge_metrics/cpbd_lv_png/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/cpbd_lv_png/many_alpha/alpha_${alpha}/
    # python3 merge_metrics/merge_data.py cpbd/output/ laplacian_variance/output/png/ merge_metrics/cpbd_lv_png/many_alpha/alpha_${alpha}/ ${alpha}
    # rm -r merge_metrics/cpbd_lv_jpg/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/cpbd_lv_jpg/many_alpha/alpha_${alpha}/
    # python3 merge_metrics/merge_data.py cpbd/output/ laplacian_variance/output/jpg/ merge_metrics/cpbd_lv_jpg/many_alpha/alpha_${alpha}/ ${alpha}
    #
    # rm -r merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/
    # python3 merge_metrics/merge_data.py cpbd/output/ Histogram-Frequency-based/output/ merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/ ${alpha}
    #
    # rm -r merge_metrics/HF_lv_png/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/HF_lv_png/many_alpha/alpha_${alpha}/
    # python3 merge_metrics/merge_data.py Histogram-Frequency-based/output/         laplacian_variance/output/png/ merge_metrics/HF_lv_png/many_alpha/alpha_${alpha}/ ${alpha}
    # rm -r merge_metrics/HF_lv_jpg/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/HF_lv_jpg/many_alpha/alpha_${alpha}/
    # python3 merge_metrics/merge_data.py Histogram-Frequency-based/output/         laplacian_variance/output/jpg/ merge_metrics/HF_lv_jpg/many_alpha/alpha_${alpha}/ ${alpha}

    # rm -r merge_metrics/cpbd_HF_lv_png/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/cpbd_HF_lv_png/many_alpha/alpha_${alpha}/
    # # python3 merge_metrics/merge_data.py merge_metrics/HF_lv_png/                  laplacian_variance/output/png/ merge_metrics/cpbd_HF_lv_png/many_alpha/alpha_${alpha}/ ${alpha}
    # python3 merge_metrics/merge_data.py merge_metrics/cpbd_HF/many_alpha/alpha_1/ laplacian_variance/output/png/ merge_metrics/cpbd_HF_lv_png/many_alpha/alpha_${alpha}/ ${alpha}
    # rm -r merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_${alpha}/
    # mkdir -p merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_${alpha}/
    # # python3 merge_metrics/merge_data.py merge_metrics/HF_lv_jpg/                  laplacian_variance/output/jpg/ merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_${alpha}/ ${alpha}
    # python3 merge_metrics/merge_data.py merge_metrics/cpbd_HF/many_alpha/alpha_1/ laplacian_variance/output/jpg/ merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_${alpha}/ ${alpha}


    # python3 visualize_output.py merge_metrics/cpbd_lv_png/many_alpha/alpha_${alpha}/    > merge_metrics/cpbd_lv_png/many_alpha/alpha_${alpha}/results.txt
    # python3 visualize_output.py merge_metrics/cpbd_lv_jpg/many_alpha/alpha_${alpha}/    > merge_metrics/cpbd_lv_jpg/many_alpha/alpha_${alpha}/results.txt
    # python3 visualize_output.py merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/        > merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/results.txt
    # python3 visualize_output.py merge_metrics/HF_lv_png/many_alpha/alpha_${alpha}/      > merge_metrics/HF_lv_png/many_alpha/alpha_${alpha}/results.txt
    # python3 visualize_output.py merge_metrics/HF_lv_jpg/many_alpha/alpha_${alpha}/      > merge_metrics/HF_lv_jpg/many_alpha/alpha_${alpha}/results.txt
    # python3 visualize_output.py merge_metrics/cpbd_HF_lv_png/many_alpha/alpha_${alpha}/ > merge_metrics/cpbd_HF_lv_png/many_alpha/alpha_${alpha}/results.txt
    # python3 visualize_output.py merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_${alpha}/ > merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_${alpha}/results.txt

    # python3 visualize_stats.py merge_metrics/cpbd_lv_png/many_alpha/alpha_${alpha}/
    # python3 visualize_stats.py merge_metrics/cpbd_lv_jpg/many_alpha/alpha_${alpha}/
    # python3 visualize_stats.py merge_metrics/cpbd_HF/many_alpha/alpha_${alpha}/
    # python3 visualize_stats.py merge_metrics/HF_lv_png/many_alpha/alpha_${alpha}/
    # python3 visualize_stats.py merge_metrics/HF_lv_jpg/many_alpha/alpha_${alpha}/
    # python3 visualize_stats.py merge_metrics/cpbd_HF_lv_png/many_alpha/alpha_${alpha}/
    # python3 visualize_stats.py merge_metrics/cpbd_HF_lv_jpg/many_alpha/alpha_${alpha}/
# done
