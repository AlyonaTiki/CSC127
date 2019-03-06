#Alyona Karmazin
#2/27/19
#this program counts snow

import matplotlib.pyplot as plt
import numpy as np

ca = input("Please enter the name of the input file: ")
countSnow = 0
t = 0.75

img = plt.imread(ca)

for i in range(img.shape[0]):
     for j in range(img.shape[1]):
          if (img[i,j,0] > t) and (img[i,j,1] > t) and (img[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)
