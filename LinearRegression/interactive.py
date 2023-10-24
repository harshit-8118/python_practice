import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import sys
sys.stdout = open('output.txt', 'w')

X = pd.read_csv('LinearRegression\X_train.csv')
Y = pd.read_csv('LinearRegression\Y_train.csv')
thetalist = np.load('LinearRegression\Thetalist.npy')
print(thetalist)

t0 = thetalist[:, 0]
t1 = thetalist[:, 1]

plt.ion()
for i in range(0, 50, 3):
    y_ = t1[i] * X + t0[i]
    plt.scatter(X, Y)
    plt.plot(X, y_, c='red')
    plt.draw()
    plt.pause(1)
    plt.clf()



