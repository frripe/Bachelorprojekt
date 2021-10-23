# chmod +x runHF.sh
# ./runHF.sh

mv Histogram-Frequency-based/output/time.txt Histogram-Frequency-based/output/time_old.txt
mv Histogram-Frequency-based/output/out_blurry.txt Histogram-Frequency-based/output/out_blurry_old.txt
mv Histogram-Frequency-based/output/out_no_problems.txt Histogram-Frequency-based/output/out_no_problems_old.txt
mv Histogram-Frequency-based/output/out_synth_no_problems.txt Histogram-Frequency-based/output/out_synth_no_problems_old.txt
mv Histogram-Frequency-based/output/out_synth_blurry.txt Histogram-Frequency-based/output/out_synth_blurry_old.txt
mv Histogram-Frequency-based/output/out_synth_blurry_gaussian_2.0.txt Histogram-Frequency-based/output/out_synth_blurry_gaussian_2.0_old.txt
mv Histogram-Frequency-based/output/out_synth_blurry_gaussian_3.0.txt Histogram-Frequency-based/output/out_synth_blurry_gaussian_3.0_old.txt
mv Histogram-Frequency-based/output/out_synth_blurry_gaussian_4.0.txt Histogram-Frequency-based/output/out_synth_blurry_gaussian_4.0_old.txt

d=1
h=0.085

for i in ../dataset/training/jpg/Blurry/*.jpg; do
#for i in {1..47}; do
    ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_blurry.txt
done
#for i in {1..34}; do
for i in ../dataset/training/jpg/NoProblems/*.jpg; do
    ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_no_problems.txt
done
#for i in {1..238}; do
for i in ../dataset/training/jpg/synth_no_problems/*.jpg; do
    ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_no_problems.txt
done
#for i in {1..329}; do
for i in ../dataset/training/jpg/synth_blurry/*.jpg; do
    ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_blurry.txt
done

#for i in {1..272}; do
for i in ../dataset/training/jpg/synth_blurry_2.0/*.jpg; do
    ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_blurry_gaussian_2.0.txt
done
#for i in {1..272}; do
for i in ../dataset/training/jpg/synth_blurry_3.0/*.jpg; do
    ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_blurry_gaussian_3.0.txt
done
#for i in {1..272}; do
for i in ../dataset/training/jpg/synth_blurry_4.0/*.jpg; do
    ./Histogram-Frequency-based/marichal-ma-zhang -d=${d} -h=${h} ${i} >> Histogram-Frequency-based/output/out_synth_blurry_gaussian_4.0.txt
done
