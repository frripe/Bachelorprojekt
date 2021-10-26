# run from software:
# python3 gen_training_and_test_set.py 0.1
import os
import shutil
import random
from sys import argv


# how big should the test set be compared to the training set
percent = float(argv[1])
types = ['jpg', 'png', 'bmp']
paths = os.listdir('../dataset/original/jpg/')
#paths = ['Blurry/', 'NoProblems/', 'synth_blurry/', 'synth_no_problems/']
random.seed(a=1)
shutil.rmtree('../dataset/test/')
shutil.rmtree('../dataset/training/')

def move(percent):
    for path in paths:
        # amount of images in the folder
        n = len(os.listdir('../dataset/original/jpg/' + path + '/'))

        tests = set()
        while len(tests) < n*percent:
            tests.add(random.randint(1, n))
        trainings = set(range(1, n)) - tests

        print(path + str(n))
        print("tests: " + str(tests))
        # print("trainings: " + str(trainings))

        for t in types:

            for im in tests:
                src_path = '../dataset/original/' + t + '/' + path + '/' + str(im) + '.' + t
                dst_path = '../dataset/test/' + t + '/' + path + '/'
                if not os.path.exists(dst_path):
                    os.makedirs(dst_path, exist_ok=True)
                shutil.copy2(src_path, dst_path + str(im) + '.' + t)

            for im in trainings:
                src_path = '../dataset/original/' + t + '/' + path + '/' + str(im) + '.' + t
                dst_path = '../dataset/training/' + t + '/' + path + '/'
                if not os.path.exists(dst_path):
                    os.makedirs(dst_path, exist_ok=True)
                shutil.copy2(src_path, dst_path + str(im) + '.' + t)

            # set without img 33 for variance of laplacian
            if t == 'png' and path in ['NoProblems', 'synth_no_problems']:
                for im in range(1, n+1):
                    src_path = '../dataset/original/' + t + '/' + path + '/' + str(im) + '.' + t
                    copy_path = t + '/' + path + '_copy/'
                    if not os.path.exists('../dataset/training/' + copy_path):
                        os.makedirs('../dataset/training/' + copy_path, exist_ok=True)
                    if not os.path.exists('../dataset/test/' + copy_path):
                        os.makedirs('../dataset/test/' + copy_path, exist_ok=True)
                    if im%34 != 33:
                        shutil.copy2(src_path, '../dataset/training/' + copy_path + str(im) + '.' + t)
                        shutil.copy2(src_path, '../dataset/test/' + copy_path + str(im) + '.' + t)

move(percent)
