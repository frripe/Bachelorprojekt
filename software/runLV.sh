# chmod +x runLV.sh
# ./runLV.sh

for type in 'jpg' 'png'; do
    mv laplacian_variance/output/${type}/time.txt                          laplacian_variance/output/${type}/time_old.txt
    mv laplacian_variance/output/${type}/out_blurry.txt                    laplacian_variance/output/${type}/out_blurry_old.txt
    mv laplacian_variance/output/${type}/out_no_problems.txt               laplacian_variance/output/${type}/out_no_problems_old.txt
    mv laplacian_variance/output/${type}/out_synth_blurry.txt              laplacian_variance/output/${type}/out_synth_blurry_old.txt
    mv laplacian_variance/output/${type}/out_synth_no_problems.txt         laplacian_variance/output/${type}/out_synth_no_problems_old.txt
    mv laplacian_variance/output/${type}/out_synth_blurry_gaussian_2.0.txt laplacian_variance/output/${type}/out_synth_blurry_gaussian_2.0_old.txt
    mv laplacian_variance/output/${type}/out_synth_blurry_gaussian_3.0.txt laplacian_variance/output/${type}/out_synth_blurry_gaussian_3.0_old.txt
    mv laplacian_variance/output/${type}/out_synth_blurry_gaussian_4.0.txt laplacian_variance/output/${type}/out_synth_blurry_gaussian_4.0_old.txt

    python3 laplacian_variance/process.py -i ../dataset/training/${type}/Blurry/                       > laplacian_variance/output/${type}/out_blurry.txt
    python3 laplacian_variance/process.py -i ../dataset/training/${type}/NoProblems_no_outlier/        > laplacian_variance/output/${type}/out_no_problems.txt
    python3 laplacian_variance/process.py -i ../dataset/training/${type}/synth_blurry/                 > laplacian_variance/output/${type}/out_synth_blurry.txt
    python3 laplacian_variance/process.py -i ../dataset/training/${type}/synth_no_problems_no_outlier/ > laplacian_variance/output/${type}/out_synth_no_problems.txt

    python3 laplacian_variance/process.py -i ../dataset/training/${type}/synth_blurry_2.0/ > laplacian_variance/output/${type}/out_synth_blurry_gaussian_2.0.txt
    python3 laplacian_variance/process.py -i ../dataset/training/${type}/synth_blurry_3.0/ > laplacian_variance/output/${type}/out_synth_blurry_gaussian_3.0.txt
    python3 laplacian_variance/process.py -i ../dataset/training/${type}/synth_blurry_4.0/ > laplacian_variance/output/${type}/out_synth_blurry_gaussian_4.0.txt
done
