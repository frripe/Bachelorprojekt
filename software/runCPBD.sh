# chmod +x runCPBD.sh
# ./runCPBD.sh

mv cpbd/output/time.txt cpbd/output/time_old.txt
mv cpbd/output/out_blurry.txt cpbd/output/out_blurry_old.txt
mv cpbd/output/out_no_problems.txt cpbd/output/out_no_problems_old.txt
mv cpbd/output/out_synth_no_problems.txt cpbd/output/out_synth_no_problems_old.txt
mv cpbd/output/out_synth_blurry.txt cpbd/output/out_synth_blurry_old.txt
mv cpbd/output/out_synth_blurry_gaussian_2.0.txt cpbd/output/out_synth_blurry_gaussian_2.0_old.txt
mv cpbd/output/out_synth_blurry_gaussian_3.0.txt cpbd/output/out_synth_blurry_gaussian_3.0_old.txt
mv cpbd/output/out_synth_blurry_gaussian_4.0.txt cpbd/output/out_synth_blurry_gaussian_4.0_old.txt


python3 cpbd/run_cpbd.py "../dataset/training/bmp/Blurry/"                       0.002 3.6 > cpbd/output/out_blurry.txt
python3 cpbd/run_cpbd.py "../dataset/training/bmp/NoProblems_no_outlier/"        0.002 3.6 > cpbd/output/out_no_problems.txt
python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_blurry/"                 0.002 3.6 > cpbd/output/out_synth_blurry.txt
python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_no_problems_no_outlier/" 0.002 3.6 > cpbd/output/out_synth_no_problems.txt

python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_blurry_2.0/"             0.002 3.6 > cpbd/output/out_synth_blurry_gaussian_2.0.txt
python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_blurry_3.0/"             0.002 3.6 > cpbd/output/out_synth_blurry_gaussian_3.0.txt
python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_blurry_4.0/"             0.002 3.6 > cpbd/output/out_synth_blurry_gaussian_4.0.txt
