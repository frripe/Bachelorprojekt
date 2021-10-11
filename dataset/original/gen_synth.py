# run from dataset:
# python3 gen_synth.py 1.5
"""
 * https://datacarpentry.org/image-processing/06-blurring/
 * Python script to demonstrate Gaussian blur.
 *
 * usage: python3 gen_synth.py <sigma>
"""
import skimage.io
import skimage.filters
import sys
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageOps

# get filename and kernel size from command line
#filename = sys.argv[1]
#sigma = float(sys.argv[2])
#sigma_x = float(sys.argv[3])
#
# read and display original image
#image = skimage.io.imread(fname=filename)
#
# apply Gaussian blur, creating a new image
#blurred = skimage.filters.gaussian(
#    image, sigma=(sigma, sigma), truncate=3.5, multichannel=True
#)
#
# display blurred image
#images = [image, blurred]
#skimage.io.imshow_collection(images)
#skimage.io.show()

s = float(sys.argv[1])
r = 15
types = ['jpg', 'png', 'bmp']

# get truncate value for desired radius (should be odd integer)
#radius = int(truncate * sigma + 0.5):          https://github.com/scipy/scipy/blob/c7ba5c0b239f10478d3c902cf4057edf1880b35d/scipy/ndimage/filters.py#L179
def get_truncate(sigma, radius):
    return (radius - 0.5)/sigma

# mirror the images with no problems
def run_mirror(fr, to, folder, synth_folder):
    for i in range(fr, to):
        for t in types:
            filename = t + '/' + folder + '/' + str(i) + '.' + t
            image = Image.open(filename)
            image_mir = ImageOps.mirror(image)
            image_flip = ImageOps.flip(image)
            image_flip_mir = ImageOps.flip(image_mir)
            image_mir.save(t + '/' + synth_folder + '/' + str(i) + '.' + t, quality=95)
            image_flip.save(t + '/' + synth_folder + '/' + str(i) + '.' + t, quality=95)
            image_flip_mir.save(t + '/' + synth_folder + '/' + str(i) + '.' + t, quality=95)

# apply blur to all images with no problems
def run_gaussian(sigma, truncate)#, fr1, to1, name1, name2, folder='NoProblems', synth_folder='synth_no_problems'):
    folder = 'NoProblems'
    synth_folder = 'synth_no_problems'
    for t in types:
        n1 = len(os.listdir(t + '/' + folder + '/'))
        for i in range(1, n1):
            filename1 = t + '/' + folder + '/' + str(i) + '.' + t
            image1 = skimage.io.imread(fname=filename1)
            blurred1 = (skimage.filters.gaussian(
                image1, sigma=(sigma, sigma), truncate=truncate, multichannel=True
            ) * 255).astype(np.uint8)
            skimage.io.imsave(t + '/synth_blurry_' + str(sigma) + '/' + str(i) + '.' + t, blurred1, check_contrast=False)

        n2 = len(os.listdir(t + '/' + folder + '/'))
        for i in range(n1, n2+n1):
            filename2 = t + '/' + synth_folder + '/' + str(i) + '.' + t
            image2 = skimage.io.imread(fname=filename2)
            blurred2 = (skimage.filters.gaussian(
                image2, sigma=(sigma, sigma), truncate=truncate, multichannel=True
            ) * 255).astype(np.uint8)
            skimage.io.imsave(t + '/synth_blurry_' + str(sigma) + '/' + str(i) + '.' + t, blurred2, check_contrast=False)

# run
run_mirror(1, 48, 'Blurry',            'synth_blurry')
run_mirror(1, 52, 'Earwax',            'synth_earwax')
run_mirror(1, 35, 'NoProblems',        'synth_no_problems')
run_mirror(1, 21, 'NoVisibleMembrane', 'synth_no_visible_membrane')
run_gaussian(s,   get_truncate(s, r))
run_gaussian(s*2, get_truncate(s*2, r))
run_gaussian(s*3, get_truncate(s*4, r))



