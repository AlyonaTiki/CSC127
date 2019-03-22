# Alyona Karmazin
# 3/12/19
# this program uses elevation data

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,2] = 0.5     #Set the blue channel to 100%
        elif elevations[row,col] == 1:
            floodMap[row, col, 0] = 0.75
            floodMap[row, col, 1] = 0.75
            floodMap[row, col, 2] = 0.75
        else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col,0] = 0.5
            floodMap[row, col, 1] = 0.5
            floodMap[row, col, 2] = 0.5


#Save the image:
plt.imsave('coast.png', floodMap)
