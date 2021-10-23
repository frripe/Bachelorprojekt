# chmod +x runFM_var.sh
# ./runFM_var.sh

mv FM/output/time.txt FM/output/time_old.txt
mv FM/output/out_blurry.txt FM/output/out_blurry_old.txt
mv FM/output/out_no_problems.txt FM/output/out_no_problems_old.txt
mv FM/output/out_synth_no_problems.txt FM/output/out_synth_no_problems_old.txt
mv FM/output/out_synth_blurry.txt  FM/output/out_synth_blurry_old.txt


#for i in {1..40}
#do
#    a=$(echo $i\*50+1 | bc)
#    rm FM/output/${a}_output_dens.png
#done
#
for i in {0..30}
do
    a=$(echo $i\*100+2 | bc)
    echo $a
    python3 FM/kanjar.py ${a} <<< "../dataset/training/png/Blurry/" > FM/output/out_blurry.txt
    python3 FM/kanjar.py ${a} <<< "../dataset/training/png/NoProblems/" > FM/output/out_no_problems.txt
    python3 FM/kanjar.py ${a} <<< "../dataset/training/png/synth_blurry/" > FM/output/out_synth_blurry.txt
    python3 FM/kanjar.py ${a} <<< "../dataset/training/png/synth_no_problems/" > FM/output/out_synth_no_problems.txt

    python3 FM/kanjar.py ${a} <<< "../dataset/training/png/synth_blurry_2.0/" > FM/output/out_synth_blurry.txt
    python3 FM/kanjar.py ${a} <<< "../dataset/training/png/synth_blurry_3.0/" > FM/output/out_synth_blurry.txt
    python3 FM/kanjar.py ${a} <<< "../dataset/training/png/synth_blurry_4.0/" > FM/output/out_synth_blurry.txt

    python3 visualize_density_plot.py FM/output/ ${a}

done
