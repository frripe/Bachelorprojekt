# freja@GLaDOS:~/Documents/DTU/bachelor/dataset$ python3 jpgToPng.py
from PIL import Image
import os

n = len(os.listdir('jpg/Blurry/'))
for n in range(1, n+1):
    im1 = Image.open(r'jpg/Blurry/' + str(n) + '.jpg')
    im1.save(r'png/Blurry/' + str(n) + '.png')

n = len(os.listdir('jpg/Earwax/'))
for n in range(1, n+1):
    im1 = Image.open(r'jpg/Earwax/' + str(n) + '.jpg')
    im1.save(r'png/Earwax/' + str(n-47) + '.png')

n = len(os.listdir('jpg/NoProblems/'))
for n in range(1, n+1):
    im1 = Image.open(r'jpg/NoProblems/' + str(n) + '.jpg')
    im1.save(r'png/NoProblems/' + str(n-98) + '.png')

n = len(os.listdir('jpg/NoVisibleMembrane/'))
for n in range(1, n+1):
    im1 = Image.open(r'jpg/NoVisibleMembrane/' + str(n) + '.jpg')
    im1.save(r'png/NoVisibleMembrane/' + str(n-132) + '.png')
