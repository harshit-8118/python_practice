import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn import linear_model
from sklearn.datasets import make_regression

import sys
sys.stdout = open('output.txt', 'w')

X = np.arange(0, 20, 1)
print(X)
noise = np.random.randn(20)
print(noise)

theta = np.array([2, 3])
y = noise
Y_ideal = theta[0]  + theta[1] * X
Y_real = Y_ideal + noise
plt.scatter(X, Y_ideal)
plt.scatter(X, y)
plt.plot(X, Y_real)
plt.show()