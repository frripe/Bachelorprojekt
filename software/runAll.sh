# chmod +x runAll.sh
# ./runAll.sh

#./runFM.sh
#./runHF.sh
#./runLV.sh
#./runCPBD.sh
#
#
#python3 merge_metrics/merge_data.py cpbd/output/ laplacian_variance/output/ merge_metrics/cpbd_lv/
#python3 merge_metrics/merge_data.py cpbd/output/ Histogram-Frequency-based/output/ merge_metrics/cpbd_HF/
#python3 merge_metrics/merge_data.py Histogram-Frequency-based/output/ laplacian_variance/output/ merge_metrics/HF_lv/
#
#python3 merge_metrics/merge_data.py merge_metrics/HF_lv/ laplacian_variance/output/ merge_metrics/cpbd_HF_lv/
#

python3 visualize_output.py Histogram-Frequency-based/output/ > Histogram-Frequency-based/output/results.txt
python3 visualize_output.py laplacian_variance/output/        > laplacian_variance/output//results.txt
python3 visualize_output.py cpbd/output/                      > cpbd/output//results.txt
python3 visualize_output.py merge_metrics/cpbd_lv/            > merge_metrics/cpbd_lv//results.txt
python3 visualize_output.py merge_metrics/cpbd_HF/            > merge_metrics/cpbd_HF//results.txt
python3 visualize_output.py merge_metrics/HF_lv/              > merge_metrics/HF_lv//results.txt
python3 visualize_output.py merge_metrics/cpbd_HF_lv/         > merge_metrics/cpbd_HF_lv//results.txt

