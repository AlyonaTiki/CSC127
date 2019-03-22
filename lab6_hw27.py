# Alyona Karmazin
# 3/6/19
# this program uses nyc data

import matplotlib.pyplot as plt
import pandas as pd


pop = pd.read_csv('nycHistPop.csv', skiprows=5)
borough = input("Enter borough: ")
output = input("Please enter the name of the output file: ")
pop['Fraction'] = pop[borough]/pop['Total']
pop.plot(x='Year', y='Fraction')

fig = plt.gcf()
fig.savefig(output)
