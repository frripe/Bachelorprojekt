# chmod +x runFM.sh
# ./runFM.sh

mv FM/output/time.txt FM/output/time_old.txt
rm FM/output/out_blurry.txt
rm FM/output/out_no_problems.txt
rm FM/output/out_synth_no_problems.txt
rm FM/output/out_synth_blurry.txt

python3 FM/kanjar.py <<< "../dataset/png/Blurry/" > FM/output/out_blurry.txt
python3 FM/kanjar.py <<< "../dataset/png/NoProblems/" > FM/output/out_no_problems.txt
python3 FM/kanjar.py <<< "../dataset/png/synth_blurry/" > FM/output/out_synth_blurry.txt
python3 FM/kanjar.py <<< "../dataset/png/synth_no_problems/" > FM/output/out_synth_no_problems.txt
