# chmod +x runCPBD_var.sh
# ./runCPBD_var.sh

mv cpbd/output/time.txt laplacian_variance/output/time_old.txt
mv cpbd/output/out_blurry.txt cpbd/output/out_blurry_old.txt
mv cpbd/output/out_no_problems.txt cpbd/output/out_no_problems_old.txt
mv cpbd/output/out_synth_no_problems.txt cpbd/output/out_synth_no_problems_old.txt
mv cpbd/output/out_synth_blurry.txt cpbd/output/out_synth_blurry_old.txt


#for b in {1..5}; do
#    c=$(echo $b\*0.05 | bc)
#    for t in {0..5}; do
#        echo $t
#        a=$(echo 0.002+$t\*0.01 | bc)
for a in 0.002 0.01 0.02 0.1 0.2 0.4; do
    for c in 0.003 0.03 0.08 0.3 3. 4.; do
        echo $a
        python3 cpbd/run_cpbd.py "../dataset/training/bmp/Blurry/" ${a} ${c} > cpbd/output/out_blurry.txt
        echo $a
        python3 cpbd/run_cpbd.py "../dataset/training/bmp/NoProblems/" ${a} ${c} > cpbd/output/out_no_problems.txt
        echo $a
        python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_blurry/" ${a} ${c} > cpbd/output/out_synth_blurry.txt
        echo $a
        python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_no_problems/" ${a} ${c} > cpbd/output/out_synth_no_problems.txt

        echo $a
        python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_blurry_2.0/" ${a} ${c} >> cpbd/output/synth_blurry.txt
        echo $a
        python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_blurry_3.0/" ${a} ${c} >> cpbd/output/synth_blurry.txt
        echo $a
        python3 cpbd/run_cpbd.py "../dataset/training/bmp/synth_blurry_4.0/" ${a} ${c} >> cpbd/output/synth_blurry.txt


        echo $a
        n="t${a}_b${c}"
        python3 visualize_density_plot.py cpbd/output/ ${n}
        echo $n
    done
done


