# python3 cpbd/run_cpbd.py ../dataset/original/bmp/Blurry/ 0.002
import os
import cpbd
import imageio
import time
from sys import argv

# folder with the images in the filesystem
path = argv[1]
THRESHOLD = float(argv[2])
#path = str(input()).rstrip()
# amount of images in the folder
n = len(os.listdir(path))

file_object = open('cpbd/output/time.txt', 'a') # added
for i in range(1, n + 1):
    time_start = time.time()
    input_image = imageio.imread(path + str(i) + '.bmp', pilmode='L')
    print(cpbd.compute(input_image, THRESHOLD))
    time_end = time.time()
    file_object.write(str(time_end - time_start) + "\n") # added # measured in seconds

