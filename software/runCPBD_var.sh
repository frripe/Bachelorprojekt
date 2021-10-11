# chmod +x runCPBD_var.sh
# ./runCPBD_var.sh

mv cpbd/output/time.txt laplacian_variance/output/time_old.txt
mv cpbd/output/out_blurry.txt cpbd/output/out_blurry_old.txt
mv cpbd/output/out_no_problems.txt cpbd/output/out_no_problems_old.txt
mv cpbd/output/out_synth_no_problems.txt cpbd/output/out_synth_no_problems_old.txt
mv cpbd/output/out_synth_blurry.txt cpbd/output/out_synth_blurry_old.txt


for i in {1..100}
do
    echo $i
    a=$(echo 0.002+$i\*0.01 | bc)
    python3 cpbd/run_cpbd.py "../dataset/original/bmp/Blurry/" ${a} > cpbd/output/out_blurry.txt
    python3 cpbd/run_cpbd.py "../dataset/original/bmp/NoProblems/" ${a} > cpbd/output/out_no_problems.txt
#    python3 cpbd/run_cpbd.py "../dataset/bmp/synth_blurry/" ${a} > cpbd/output/out_synth_blurry.txt
    python3 cpbd/run_cpbd.py "../dataset/original/bmp/synth_no_problems/" ${a} > cpbd/output/out_synth_no_problems.txt
    echo $a
    python3 visualize_density_plot.py cpbd/output/ ${a}
    echo $a
    
done



