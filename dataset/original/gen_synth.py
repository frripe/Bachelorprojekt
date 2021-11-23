# run from dataset:
# python3 original/gen_synth.py 2
"""
 * https://datacarpentry.org/image-processing/06-blurring/
 * Python script to demonstrate Gaussian blur.
 *
 * usage: python3 gen_synth.py <sigma>
"""
import skimage.io
import skimage.filters
import sys
import os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageOps

# get kernel size from command line
s = float(sys.argv[1])
r = 15
types = ['jpg']#['jpg', 'png', 'bmp']

# get truncate value for desired radius (should be odd integer)
#radius = int(truncate * sigma + 0.5):          https://github.com/scipy/scipy/blob/c7ba5c0b239f10478d3c902cf4057edf1880b35d/scipy/ndimage/filters.py#L179
def get_truncate(sigma, radius):
    return (radius - 0.5)/sigma

# mirror the images with no problems
def run_mirror(fr, to, folder, synth_folder):
    for i in range(fr, to):
        for t in types:
            filename = 'original/' + t + '/' + folder + '/' + str(i).zfill(4) + '.' + t
            image = Image.open(filename)
            image_mir = ImageOps.mirror(image)
            image_flip = ImageOps.flip(image)
            image_flip_mir = ImageOps.flip(image_mir)
            image_mir.save('original/' + t + '/' + synth_folder + '/' + str(i).zfill(4) + '.' + t)
            image_flip.save('original/' + t + '/' + synth_folder + '/' + str(i+(to-1)).zfill(4) + '.' + t)
            image_flip_mir.save('original/' + t + '/' + synth_folder + '/' + str(i+(to-1)*2).zfill(4) + '.' + t)
            # for a in(1, 3):
            image_rot1 = image.rotate(5)
            image_rot2 = image.rotate(-5)
            image_rot1.save('original/' + t + '/' + synth_folder + '/' + str(i+(to-1)*3).zfill(4) + '.' + t)
            image_rot2.save('original/' + t + '/' + synth_folder + '/' + str(i+(to-1)*4).zfill(4) + '.' + t)
            image_rot1 = image.rotate(2*5)
            image_rot2 = image.rotate(-2*5)
            image_rot1.save('original/' + t + '/' + synth_folder + '/' + str(i+(to-1)*5).zfill(4) + '.' + t)
            image_rot2.save('original/' + t + '/' + synth_folder + '/' + str(i+(to-1)*6).zfill(4) + '.' + t)

# apply blur to all images with no problems
def run_gaussian(sigma, truncate):
    print("gauss: ", sigma)
    folder = 'NoProblems'
    synth_folder = 'synth_no_problems'
    for t in types:
        print(t)
        path = 'original/' + t + '/synth_blurry_' + str(sigma) + '/'
        if not os.path.exists(path):
            os.mkdir(path)
        n1 = min(32, len(os.listdir('original/' + t + '/' + folder + '/')))
        for i in range(1, n1+1):
            filename = 'original/' + t + '/' + folder + '/' + str(i).zfill(4) + '.' + t
            image = skimage.io.imread(fname=filename)
            blurred = (skimage.filters.gaussian(
                image, sigma=(sigma, sigma), truncate=truncate, multichannel=True
            ) * 255).astype(np.uint8)
            skimage.io.imsave(path + str(i).zfill(4) + '.' + t, blurred, check_contrast=False)

        n2 = min(32, len(os.listdir('original/' + t + '/' + synth_folder + '/')))
        for i in range(1, n2+1):
            filename = 'original/' + t + '/' + synth_folder + '/' + str(i).zfill(4) + '.' + t
            image = skimage.io.imread(fname=filename)
            blurred = (skimage.filters.gaussian(
                image, sigma=(sigma, sigma), truncate=truncate, multichannel=True
            ) * 255).astype(np.uint8)
            skimage.io.imsave(path + str(i+n1).zfill(4) + '.' + t, blurred, check_contrast=False)

# run
run_mirror(1, 48, 'Blurry',     'synth_blurry')
#run_mirror(1, 52, 'Earwax',   'synth_earwax')
run_mirror(1, 35, 'NoProblems', 'synth_no_problems')
#run_mirror(1, 21, 'NoVisibleMembrane', 'synth_no_visible_membrane')
run_gaussian(s,     get_truncate(s, r))
run_gaussian(s*1.5, get_truncate(s*1.5, r))
run_gaussian(s*2,   get_truncate(s*2, r))
