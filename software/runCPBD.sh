# chmod +x runCPBD.sh
# ./runCPBD.sh

mv cpbd/output/time.txt cpbd/output/time_old.txt
rm cpbd/output/out_blurry.txt
rm cpbd/output/out_no_problems.txt
rm cpbd/output/out_synth_no_problems.txt
rm cpbd/output/out_synth_blurry.txt

mv cpbd/output/time.txt cpbd/output/time_old.txt
python3 cpbd/run_cpbd.py <<< "../dataset/bmp/Blurry/" > cpbd/output/out_blurry.txt
python3 cpbd/run_cpbd.py <<< "../dataset/bmp/NoProblems/" > cpbd/output/out_no_problems.txt
python3 cpbd/run_cpbd.py <<< "../dataset/bmp/synth_blurry/" > cpbd/output/out_synth_blurry.txt
python3 cpbd/run_cpbd.py <<< "../dataset/bmp/synth_no_problems/" > cpbd/output/out_synth_no_problems.txt

