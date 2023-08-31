#股票相关  开盘价和最高价

import numpy as np
import matplotlib.pyplot as plt

open,maxmize = np.loadtxt('ss12.csv',delimiter=',',skiprows=1,usecols=(1,2),unpack=True)
change = maxmize - open
yesterday = change[:-1]
today = change[1:]
plt.scatter(yesterday,today,s=20,c='r',marker='^',alpha=0.5)
plt.show()