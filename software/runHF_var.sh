# chmod +x runHF_var.sh
# ./runHF_var.sh

for d in {0..5}; do
    for h in 0.005 0.01 0.05 0.06 0.07 0.08 0.085 0.09 0.1 0.11 0.12 0.5 0.9; do
        mv Histogram-Frequency-based/output/time.txt Histogram-Frequency-based/output/time_old.txt
        mv Histogram-Frequency-based/output/out_blurry.txt Histogram-Frequency-based/output/out_blurry_old.txt
        mv Histogram-Frequency-based/output/out_no_problems.txt Histogram-Frequency-based/output/out_no_problems_old.txt
        mv Histogram-Frequency-based/output/out_synth_no_problems.txt Histogram-Frequency-based/output/out_synth_no_problems_old.txt
        mv Histogram-Frequency-based/output/out_synth_blurry.txt Histogram-Frequency-based/output/out_synth_blurry_old.txt

#        mv Histogram-Frequency-based/output/out_synth_blurry_1.5.txt Histogram-Frequency-based/output/out_synth_blurry_2.0_old.txt
#        mv Histogram-Frequency-based/output/out_synth_blurry_3.0.txt Histogram-Frequency-based/output/out_synth_blurry_3.0_old.txt
#        mv Histogram-Frequency-based/output/out_synth_blurry_4.5.txt Histogram-Frequency-based/output/out_synth_blurry_4.0_old.txt


        for i in ../dataset/training/jpg/Blurry/*.jpg; do
            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_blurry.txt
        done

        for i in ../dataset/training/jpg/NoProblems/*.jpg; do
            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_no_problems.txt
        done

        for i in ../dataset/training/jpg/synth_no_problems/*.jpg; do
            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_no_problems.txt
        done

        for i in ../dataset/training/jpg/synth_blurry/*.jpg; do
            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_blurry.txt
        done


#        for i in ../dataset/training/jpg/synth_blurry_2.0/*.jpg; do
#            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_blurry.txt
#        done
#        for i in ../dataset/training/jpg/synth_blurry_3.0/*.jpg; do
#            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_blurry.txt
#        done
#        for i in ../dataset/training/jpg/synth_blurry_4.0/*.jpg; do
#            ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_blurry.txt
#        done
#
#        
        a="min${d}_max${h}"
        python3 visualize_density_plot.py Histogram-Frequency-based/output/ ${a}
        echo ${a}
#
    done
done
