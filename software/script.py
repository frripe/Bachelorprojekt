import sys
import subprocess
img = '../dataset/test/jpg/synth_no_problems_no_outlier/0134.jpg'
# result = subprocess.call(['./metrics_and_training_code/Histogram-Frequency-based/marichal-ma-zhang', '-d=1', '-h=0.085', '-t=0', img])
result = subprocess.check_output(['./metrics_and_training_code/Histogram-Frequency-based/marichal-ma-zhang', '-d=1', '-h=0.085', '-t=0', img])
print(result.decode())

# print(subprocess.Popen(['./metrics_and_training_code/Histogram-Frequency-based/marichal-ma-zhang', '-d=1', '-h=0.085', img], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).communicate())
# score = subprocess.check_output(['./metrics_and_training_code/Histogram-Frequency-based/marichal-ma-zhang', '-d=1', '-h=0.085', img])
# score.stdin.write("1\n")
# score.stdin.flush()
# returncode = score.wait()
# print(process.stdout.read())
