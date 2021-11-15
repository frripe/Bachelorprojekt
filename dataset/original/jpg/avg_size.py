import os
from PIL import Image

avg_w = []
avg_h = []
# print([name for name in os.listdir('.') if os.path.isdir('./' + name)])
# for foldername in [name for name in os.listdir('.') if os.path.isdir('./' + name)]:
for foldername in ['synth_blurry', 'synth_no_problems', 'Blurry', 'NoProblems']:
    n = len(os.listdir(foldername + '/'))
    print(foldername, n)
    sum_w, sum_h = 0, 0
    for n in range(1, n+1):
        image = Image.open(foldername + '/' + str(n).zfill(4) + '.jpg', 'r')
        width, height = image.size
        # print(width, height)
        sum_w += width
        sum_h += height
    if n:
        sum_w = sum_w/n
        sum_h = sum_h/n
    avg_w.append(sum_w)
    avg_h.append(sum_h)

print(sum(avg_w)/len(avg_w))
print(sum(avg_w)/len(avg_w))
