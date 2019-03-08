# Alyona Karmazin
# 3/6/19
# this program converts kilometers to miles

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
print(pop)
pop.plot(x="Year")
plt.show()