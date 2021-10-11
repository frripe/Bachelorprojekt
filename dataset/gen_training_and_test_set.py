# run from dataset:
# python3 gen_training_and_test_set.py 0.1
import os
import shutil
import random
from sys import argv


# how big should the test set be compared to the training set
percent = float(argv[1])
types = ['jpg', 'png', 'bmp']
paths = os.listdir('original/jpg/')
#paths = ['Blurry/', 'NoProblems/', 'synth_blurry/', 'synth_no_problems/']
random.seed(a=1)

def move(percent):
    for t in types:
        for path in paths:
            # amount of images in the folder
#            print(path)
            n = len(os.listdir('original/' + t + '/' + path + '/'))
            tests = set()
            while len(tests) < n*percent:
                tests.add(random.randint(1, n))
            
            trainings = set(range(1, n)) - tests
            
#            print("n: " + str(n))
#            print("tests: " + str(tests))
#            print("trainings: " + str(trainings))

            for im in tests:
                src_path = 'original/' + t + '/' + path + '/' + str(im) + '.' + t
                dst_path = 'test/' + t + '/' + path + '/'
                if not os.path.exists(dst_path):
                    os.mkdir(dst_path)
                shutil.copy2(src_path, dst_path + str(im) + '.' + t)

            for im in trainings:
                src_path = 'original/' + t + '/' + path + '/' + str(im) + '.' + t
                dst_path = 'training/' + t + '/' + path + '/'
                if not os.path.exists(dst_path):
                    os.mkdir(dst_path)
                shutil.copy2(src_path, dst_path + str(im) + '.' + t)
    
move(percent)

