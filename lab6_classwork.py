# Alyona Karmazin
# 3/6/19
# this program uses nyc data

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
borough = input("Enter borough: ")
print("Maximum population:", pop[borough].max())
print("Average population:", pop[borough].mean())



