# chmod +x runLV.sh
# ./runLV.sh

mv laplacian_variance/output/time.txt laplacian_variance/output/time_old.txt
rm laplacian_variance/output/out_blurry.txt
rm laplacian_variance/output/out_no_problems.txt
rm laplacian_variance/output/out_synth_no_problems.txt
rm laplacian_variance/output/out_synth_blurry.txt

python3 laplacian_variance/process.py -i ../dataset/jpg/NoProblems/ > laplacian_variance/output/out_no_problems.txt
python3 laplacian_variance/process.py -i ../dataset/jpg/Blurry/ > laplacian_variance/output/out_blurry.txt
python3 laplacian_variance/process.py -i ../dataset/jpg/synth_blurry/ > laplacian_variance/output/out_synth_blurry.txt
python3 laplacian_variance/process.py -i ../dataset/jpg/synth_no_problems/ > laplacian_variance/output/out_synth_no_problems.txt

