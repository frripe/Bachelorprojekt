# chmod +x runFM.sh
# ./runFM.sh

mv FM/output/time.txt                          FM/output/time_old.txt
mv FM/output/out_blurry.txt                    FM/output/out_blurry_old.txt
mv FM/output/out_no_problems.txt               FM/output/out_no_problems_old.txt
mv FM/output/out_synth_blurry.txt              FM/output/out_synth_blurry_old.txt
mv FM/output/out_synth_no_problems.txt         FM/output/out_synth_no_problems_old.txt
mv FM/output/out_synth_blurry_gaussian_2.0.txt FM/output/out_synth_blurry_gaussian_2.0_old.txt
mv FM/output/out_synth_blurry_gaussian_3.0.txt FM/output/out_synth_blurry_gaussian_3.0_old.txt
mv FM/output/out_synth_blurry_gaussian_4.0.txt FM/output/out_synth_blurry_gaussian_4.0_old.txt

python3 FM/kanjar.py 102 <<< "../dataset/training/png/Blurry/"                       > FM/output/out_blurry.txt
python3 FM/kanjar.py 102 <<< "../dataset/training/png/NoProblems_no_outlier/"        > FM/output/out_no_problems.txt
python3 FM/kanjar.py 102 <<< "../dataset/training/png/synth_blurry/"                 > FM/output/out_synth_blurry.txt
python3 FM/kanjar.py 102 <<< "../dataset/training/png/synth_no_problems_no_outlier/" > FM/output/out_synth_no_problems.txt

python3 FM/kanjar.py 102 <<< "../dataset/training/png/synth_blurry_2.0/" > FM/output/out_synth_blurry_gaussian_2.0.txt
python3 FM/kanjar.py 102 <<< "../dataset/training/png/synth_blurry_3.0/" > FM/output/out_synth_blurry_gaussian_3.0.txt
python3 FM/kanjar.py 102 <<< "../dataset/training/png/synth_blurry_4.0/" > FM/output/out_synth_blurry_gaussian_4.0.txt
