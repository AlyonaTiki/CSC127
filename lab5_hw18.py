#Alyona Karmazin
#2/27/19
#this program creates an image of red and white stripes

import numpy as np
import matplotlib.pyplot as plt

num = int(input("Enter the size: "))
out = input("Enter the output file name: ")
img = np.ones((num,num,3))
img[::2,:,1:] = 0
#filename = out + ".png"

plt.imsave(out, img)