# chmod +x runCPBD.sh
# ./runCPBD.sh

mv cpbd/output/time.txt cpbd/output/time_old.txt
rm cpbd/output/out_blurry.txt
rm cpbd/output/out_no_problems.txt
rm cpbd/output/out_synth_no_problems.txt
rm cpbd/output/out_synth_blurry.txt

mv cpbd/output/time.txt cpbd/output/time_old.txt
python3 cpbd/run_cpbd.py "../dataset/training/bmp/Blurry/" 0.002 > cpbd/output/out_blurry.txt
python3 cpbd/run_cpbd.py "../dataset/training/bmp/NoProblems/" 0.002 > cpbd/output/out_no_problems.txt
python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_blurry/" 0.002 > cpbd/output/out_synth_blurry.txt
python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_no_problems/" 0.002 > cpbd/output/out_synth_no_problems.txt

