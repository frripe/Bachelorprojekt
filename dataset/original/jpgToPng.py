# freja@GLaDOS:~/Documents/DTU/bachelor/dataset$ python3 jpgToPng.py 
from PIL import Image

for n in range(1,48):
    im1 = Image.open(r'jpg/Blurry/' + str(n) + '.jpg')
    im1.save(r'png/Blurry/' + str(n) + '.png')
    
for n in range(48,99):
    im1 = Image.open(r'jpg/Earwax/' + str(n) + '.jpg')
    im1.save(r'png/Earwax/' + str(n-47) + '.png')

for n in range(99,133):
    im1 = Image.open(r'jpg/NoProblems/' + str(n) + '.jpg')
    im1.save(r'png/NoProblems/' + str(n-98) + '.png')

for n in range(133,154):
    im1 = Image.open(r'jpg/NoVisibleMembrane/' + str(n) + '.jpg')
    im1.save(r'png/NoVisibleMembrane/' + str(n-132) + '.png')
