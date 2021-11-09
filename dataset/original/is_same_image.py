import cv2
import numpy as np
from PIL import Image

imgjpg = Image.open("jpg/Blurry/0001.jpg")
imgjpg = np.asarray(imgjpg)
img2jpg = cv2.imread("jpg/Blurry/0001.jpg")

imgpng = Image.open("png/Blurry/0001.png")
imgpng = np.asarray(imgpng)
img2png = cv2.imread("png/Blurry/0001.png")


if np.all((np.subtract(imgjpg, imgpng) == 0)) == False:
    print("pillow opens jpg and png differently")
    print(np.subtract(imgjpg, imgpng))
if np.all((np.subtract(img2jpg, img2png) == 0)) == False:
    print("cv2 opens jpg and png differently")
    # print(np.subtract(img2jpg, img2png))
#     for elem in np.subtract(img2jpg, img2png):
#         for e in elem:
#             if np.all(e == 0):
#                 continue
#             else:
#                 print(e)
if np.all((np.subtract(imgjpg, img2jpg[...,::-1].copy()) == 0)) == False:
    print("jpg opens different for pillow and cv2")
    # for elem in np.subtract(img2jpg, imgjpg, img2jpg[...,::-1].copy()):
    #     for e in elem:
    #         if np.all(e == 0):
    #             continue
    #         else:
    #             print(e)
if np.all((np.subtract(imgpng, img2png[...,::-1].copy()) == 0)) == False:
    print("png opens different for pillow and cv2")
