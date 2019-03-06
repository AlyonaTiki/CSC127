#Alyona Karmazin
#2/20/19
#this program asks user to input message, then prints it with encryption by shifting letters to right 13 times

import matplotlib.pyplot as plt

imgInput = input("Please enter the name of the input file: ")
imgOutput = input("Please enter the name of the output file: ")

img = plt.imread(imgInput)   #Read in image from csBridge.png


img2 = img.copy()        #make a copy of our image
img2[:,:,1] = 0          #Set the green channel to 0



plt.imsave(imgOutput, img2)  #Save the image we created to the file: reds.png