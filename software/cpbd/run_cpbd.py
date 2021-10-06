import os
import cpbd
import imageio
import time

# folder with the images in the filesystem
path = str(input()).rstrip()

# amount of images in the folder
n = len(os.listdir(path))

file_object = open('cpbd/output/time.txt', 'a') # added
for i in range(1, n + 1):
    time_start = time.time()
    input_image = imageio.imread(path + str(i) + '.bmp', pilmode='L')
    print(cpbd.compute(input_image))
    time_end = time.time()
    file_object.write(str(time_end - time_start) + "\n") # added # measured in seconds

