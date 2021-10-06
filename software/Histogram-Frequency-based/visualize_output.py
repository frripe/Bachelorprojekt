import matplotlib.pyplot as plt
import numpy as np
import time

x1 = list(range(1, 48))
y1=[]
with open('Histogram-Frequency-based/output/out_blur.txt', 'r') as file:
    y1 = file.read()
    y1 = [float(i) for i in y1.split()]
print(y1)

x2 = list(range(99, 132))
y2=[]
with open('Histogram-Frequency-based/output/out_no_problems.txt', 'r') as file:
    y2 = file.read()
    y2 = [float(i) for i in y2.split()]
print(y2)

plt.plot(x1,y1, 'o-', label = 'Blurry')
plt.plot(x2,y2, 'o-', label = 'No problems')
plt.title("Histogram frequency-based metric") 
plt.xlabel("Image no.") 
plt.ylabel("Score") 
plt.legend()
plt.savefig('cpbd/output/output_cpbd.png')


