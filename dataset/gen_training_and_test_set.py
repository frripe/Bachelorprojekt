# run from dataset:
# python3 gen_training_and_test_set.py 0.1
import os
import shutil
import random
from sys import argv


# how big should the test set be compared to the training set
percent = float(argv[1])
types = ['jpg', 'png', 'bmp']
paths = ['Blurry/', 'NoProblems/', 'synth_blurry/', 'synth_no_problems/']
random.seed(a=1)

def move(percent):
    for t in types:
        for path in paths:
            # amount of images in the folder
            n = len(os.listdir('original/' + t + '/' + path))
            tests = set()
            while len(tests) < n*percent:
                tests.add(random.randint(1, n))
            
            trainings = set(range(1, n)) - tests

            for im in tests:
                src_path = 'original/' + t + '/' + path + str(im) + '.' + t
                dst_path = 'test/' + t + '/' + path + str(im) + '.' + t
                shutil.copy2(src_path, dst_path)

            for im in trainings:
                src_path = 'original/' + t + '/' + path + str(im) + '.' + t
                dst_path = 'training/' + t + '/' + path + str(im) + '.' + t
                shutil.copy2(src_path, dst_path)
    
move(percent)

