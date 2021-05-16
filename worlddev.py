import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("worlddev.csv", index_col = 0)

# Dataframe Variables
pop = df[['population']]
cont = df[['continent']]
life_exp = df[['life_exp']]
gdp = df[['gdp_cap']]

# Scatter Plot Setup
plt.scatter(gdp, life_exp, s = pop / 1000000)
plt.xscale('log')

# Graph Labels
xlab = 'GDP per Capita (USD)'
ylab = 'Life Expectancy (Years)'
title = 'World Development in 2007'
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)

# Graph Intervals
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
plt.xticks(tick_val, tick_lab)

# Print Scatter Plot
plt.show

# Subsetting Dataframe Categorically
lifeexp_series = df['life_exp']
gdp_series = df['gdp_cap']
low_dev = np.logical_and(gdp_series < 12536, lifeexp_series < 70)
high_dev = np.logical_and(gdp_series >= 12536, lifeexp_series >= 70)
