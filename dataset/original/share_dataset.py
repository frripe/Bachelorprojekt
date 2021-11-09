# python3 ../dataset/original/share_dataset.py
from PIL import Image, ImageChops
import os

path = '../dataset/original/'
print([name for name in os.listdir(path + 'jpg/') if os.path.isdir(path + 'jpg/' + name)])

for foldername in [name for name in os.listdir(path + 'jpg/') if os.path.isdir(path + 'jpg/' + name)]:
    n = len(os.listdir(path + 'jpg/' + foldername + '/'))
    print(foldername, n)
    for n in range(1, n+1):
        im1 = Image.open(path + 'jpg/' + foldername + '/' + str(n).zfill(4) + '.jpg', 'r')
        im1.save(path + 'png/' + foldername + '/' + str(n).zfill(4) + '.png')
        im1.save(path + 'bmp/' + foldername + '/' + str(n).zfill(4) + '.bmp')

        # images identical check
        im_png = Image.open(path + 'png/' + foldername + '/' + str(n).zfill(4) + '.png')
        im_bmp = Image.open(path + 'bmp/' + foldername + '/' + str(n).zfill(4) + '.bmp')
        diffp = ImageChops.difference(im1, im_png)
        diffb = ImageChops.difference(im1, im_bmp)
        if diffp.getbbox() or diffb.getbbox():
            print("images " + str(n).zfill(4) + " are different")
