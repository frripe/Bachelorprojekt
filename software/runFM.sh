# chmod +x runFM.sh
# ./runFM.sh

mv FM/output/time.txt FM/output/time_old.txt
mv FM/output/out_blurry.txt FM/output/out_blurry_old.txt
mv FM/output/out_no_problems.txt FM/output/out_no_problems_old.txt
mv FM/output/out_synth_no_problems.txt FM/output/out_synth_no_problems_old.txt
mv FM/output/out_synth_blurry.txt FM/output/out_synth_blurry_old.txt

python3 FM/kanjar.py <<< "../dataset/training/png/Blurry/" > FM/output/out_blurry.txt
python3 FM/kanjar.py <<< "../dataset/training/png/NoProblems/" > FM/output/out_no_problems.txt
python3 FM/kanjar.py <<< "../dataset/training/png/synth_blurry/" > FM/output/out_synth_blurry.txt
python3 FM/kanjar.py <<< "../dataset/training/png/synth_no_problems/" > FM/output/out_synth_no_problems.txt
