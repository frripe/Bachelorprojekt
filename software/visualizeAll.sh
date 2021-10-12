# chmod +x visualizeAll.sh
# ./visualizeAll.sh

python3 visualize_output.py Histogram-Frequency-based/output/
python3 visualize_output.py cpbd/output/
python3 visualize_output.py laplacian_variance/output/
python3 visualize_output.py FM/output/
python3 visualize_output.py merge_metrics/cpbd_lv/
python3 visualize_output.py merge_metrics/cpbd_HF/
python3 visualize_output.py merge_metrics/HF_lv/
python3 visualize_output.py merge_metrics/cpbd_HF_lv/

