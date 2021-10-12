# python3 cpbd/run_cpbd.py ../dataset/original/bmp/Blurry/ 0.002 3.6
import os
import cpbd
import imageio
import time
from sys import argv

# folder with the images in the filesystem
path = argv[1]
THRESHOLD = float(argv[2])
BETA = float(argv[3])
#path = str(input()).rstrip()
# images in the folder
n = os.listdir(path)

file_object = open('cpbd/output/time.txt', 'a') # added
#for i in range(1, n + 1):
for i in n:
    time_start = time.time()
    input_image = imageio.imread(path + i, pilmode='L')
    print(cpbd.compute(input_image, THRESHOLD, BETA))
    time_end = time.time()
    file_object.write(str(time_end - time_start) + "\n") # added # measured in seconds

