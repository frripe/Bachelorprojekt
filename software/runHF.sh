# chmod +x runHF.sh
# ./runHF.sh

mv Histogram-Frequency-based/output/time.txt Histogram-Frequency-based/output/time_old.txt
mv Histogram-Frequency-based/output/out_blurry.txt Histogram-Frequency-based/output/out_blurry_old.txt
mv Histogram-Frequency-based/output/out_no_problems.txt Histogram-Frequency-based/output/out_no_problems_old.txt
mv Histogram-Frequency-based/output/out_synth_no_problems.txt Histogram-Frequency-based/output/out_synth_no_problems_old.txt
mv Histogram-Frequency-based/output/out_synth_blurry.txt Histogram-Frequency-based/output/out_synth_blurry_old.txt

for i in {1..47}
do
    ./Histogram-Frequency-based/marichal-ma-zhang "../dataset/jpg/Blurry/${i}.jpg" >> Histogram-Frequency-based/output/out_blurry.txt
done

for i in {1..34}
do
    ./Histogram-Frequency-based/marichal-ma-zhang "../dataset/jpg/NoProblems/${i}.jpg" >> Histogram-Frequency-based/output/out_no_problems.txt
done

for i in {1..34}
do
    ./Histogram-Frequency-based/marichal-ma-zhang "../dataset/jpg/synth_no_problems/${i}.jpg" >> Histogram-Frequency-based/output/out_synth_no_problems.txt
done

for i in {1..251}
do
    ./Histogram-Frequency-based/marichal-ma-zhang "../dataset/jpg/synth_blurry/${i}.jpg" >> Histogram-Frequency-based/output/out_synth_blurry.txt
done

