# chmod +x runHF_var.sh
# ./runHF_var.sh

for d in {1..10}
do
    for h in 0.0001 0.0005 0.001 0.002 0.003 0.004 0.005 0.01 0.05 0.1 0.5 1
    do
        mv Histogram-Frequency-based/output/time.txt Histogram-Frequency-based/output/time_old.txt
        mv Histogram-Frequency-based/output/out_blurry.txt Histogram-Frequency-based/output/out_blurry_old.txt
        mv Histogram-Frequency-based/output/out_no_problems.txt Histogram-Frequency-based/output/out_no_problems_old.txt
        mv Histogram-Frequency-based/output/out_synth_no_problems.txt Histogram-Frequency-based/output/out_synth_no_problems_old.txt
#        mv Histogram-Frequency-based/output/out_synth_blurry.txt Histogram-Frequency-based/output/out_synth_blurry_old.txt

        for i in {1..47}
        do
            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} "../dataset/original/jpg/Blurry/${i}.jpg" >> Histogram-Frequency-based/output/out_blurry.txt
        done

        for i in {1..34}
        do
            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} "../dataset/original/jpg/NoProblems/${i}.jpg" >> Histogram-Frequency-based/output/out_no_problems.txt
        done

        for i in {1..34}
        do
            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} "../dataset/original/jpg/synth_no_problems/${i}.jpg" >> Histogram-Frequency-based/output/out_synth_no_problems.txt
        done

#        for i in {1..251}
#        do
#            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} "../dataset/original/jpg/synth_blurry/${i}.jpg" >> Histogram-Frequency-based/output/out_synth_blurry.txt
#        done
        a="min${d}_max${h}"
        python3 visualize_density_plot.py Histogram-Frequency-based/output/ ${a}
        echo ${a}

    done
done
