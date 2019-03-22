# Alyona Karmazin
# 3/12/19
# this program crops image

import matplotlib.pyplot as plt

inF = input("Enter image file name: ")
out = input("Enter output file: ")
img = plt.imread(inF)
height = img.shape[0]
width = img.shape[1]
img2 = img[:height//2, width//2:]
plt.imsave(out, img2)
