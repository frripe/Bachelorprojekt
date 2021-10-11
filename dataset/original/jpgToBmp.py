# freja@GLaDOS:~/Documents/DTU/bachelor/dataset$ python3 jpgToBmp.py 
from PIL import Image

for n in range(1,48):
    im1 = Image.open(r'jpg/Blurry/' + str(n) + '.jpg')
    im1.save(r'bmp/Blurry/' + str(n) + '.bmp')
    
for n in range(48,99):
    im1 = Image.open(r'jpg/Earwax/' + str(n) + '.jpg')
    im1.save(r'bmp/Earwax/' + str(n-47) + '.bmp')

for n in range(99,133):
    im1 = Image.open(r'jpg/NoProblems/' + str(n) + '.jpg')
    im1.save(r'bmp/NoProblems/' + str(n-98) + '.bmp')

for n in range(133,154):
    im1 = Image.open(r'jpg/NoVisibleMembrane/' + str(n) + '.jpg')
    im1.save(r'bmp/NoVisibleMembrane/' + str(n-132) + '.bmp')
