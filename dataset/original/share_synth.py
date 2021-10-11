# python3 share_synth.py
from PIL import Image
import os

n = len(os.listdir('original/png/synth_blurry/'))
for n in range(1, n+1):
    im1 = Image.open(r'original/png/synth_blurry/' + str(n) + '.png')
    im1.save(r'original/jpg/synth_blurry/' + str(n) + '.jpg')
    im1.save(r'original/bmp/synth_blurry/' + str(n) + '.bmp')
    
n = len(os.listdir('original/png/synth_no_problems/'))
for n in range(1, n+1):
    im1 = Image.open(r'original/png/synth_no_problems/' + str(n) + '.png')
    im1.save(r'original/jpg/synth_no_problems/' + str(n) + '.jpg')
    im1.save(r'original/bmp/synth_no_problems/' + str(n) + '.bmp')

n = len(os.listdir('original/png/synth_blurry_2.0/'))
for n in range(1, n+1):
    im1 = Image.open(r'original/png/synth_blurry_2.0/' + str(n) + '.png')
    im1.save(r'original/jpg/synth_blurry_2.0/' + str(n) + '.jpg')
    im1.save(r'original/bmp/synth_blurry_2.0/' + str(n) + '.bmp')
n = len(os.listdir('original/png/synth_blurry_3.0/'))
for n in range(1, n+1):
    im1 = Image.open(r'original/png/synth_blurry_3.0/' + str(n) + '.png')
    im1.save(r'original/jpg/synth_blurry_3.0/' + str(n) + '.jpg')
    im1.save(r'original/bmp/synth_blurry_3.0/' + str(n) + '.bmp')
n = len(os.listdir('original/png/synth_blurry_4.0/'))
for n in range(1, n+1):
    im1 = Image.open(r'original/png/synth_blurry_4.0/' + str(n) + '.png')
    im1.save(r'original/jpg/synth_blurry_4.0/' + str(n) + '.jpg')
    im1.save(r'original/bmp/synth_blurry_4.0/' + str(n) + '.bmp')


