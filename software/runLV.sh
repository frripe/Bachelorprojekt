# chmod +x runLV.sh
# ./runLV.sh

mv laplacian_variance/output/time.txt laplacian_variance/output/time_old.txt
mv laplacian_variance/output/out_blurry.txt laplacian_variance/output/out_blurry_old.txt
mv laplacian_variance/output/out_no_problems.txt laplacian_variance/output/out_no_problems_old.txt
mv laplacian_variance/output/out_synth_no_problems.txt laplacian_variance/output/out_synth_no_problems_old.txt
mv laplacian_variance/output/out_synth_blurry.txt laplacian_variance/output/out_synth_blurry_old.txt
mv laplacian_variance/output/out_synth_blurry_gaussian.txt laplacian_variance/output/out_synth_blurry_gaussian_old.txt

python3 laplacian_variance/process.py -i ../dataset/training/png/NoProblems/ > laplacian_variance/output/out_no_problems.txt
python3 laplacian_variance/process.py -i ../dataset/training/png/Blurry/ > laplacian_variance/output/out_blurry.txt
python3 laplacian_variance/process.py -i ../dataset/training/png/synth_blurry/ > laplacian_variance/output/out_synth_blurry.txt
python3 laplacian_variance/process.py -i ../dataset/training/png/synth_no_problems/ > laplacian_variance/output/out_synth_no_problems.txt

python3 laplacian_variance/process.py -i ../dataset/training/png/synth_blurry_2.0/ >> laplacian_variance/output/out_synth_blurry_gaussian_2.0.txt
python3 laplacian_variance/process.py -i ../dataset/training/png/synth_blurry_3.0/ >> laplacian_variance/output/out_synth_blurry_gaussian_3.0.txt
python3 laplacian_variance/process.py -i ../dataset/training/png/synth_blurry_4.0/ >> laplacian_variance/output/out_synth_blurry_gaussian_4.0.txt
