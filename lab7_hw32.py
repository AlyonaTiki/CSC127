# Alyona Karmazin
# 3/21/19
# this program uses nyc data

import matplotlib.pyplot as plt
import pandas as pd

inFile = input("Enter name of input: ")

outFile = input("Enter name of output file: ")
homeless = pd.read_csv(inFile)
homeless['Fraction Children'] = homeless["Total Children in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Children")
#plt.show()

fig = plt.gcf()
fig.savefig(outFile)