# chmod +x runTests.sh
# ./runTests.sh

for f in 0.02 0.1 0.3 0.7; do
    python3 run.py -t -q 0 -f ${f}
done
# for f in 0.02 0.1 0.3 0.7; do
#     python3 run.py -t -q 1 -f ${f}
# done
