import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import sys
sys.stdout = open('output.txt', 'w')

mean = np.array([0.0, 1.0])
cov = np.array([[1.0, 0.6], [0.6, 1.0]])

dist = np.random.multivariate_normal(mean, cov, 300)
print(dist)
y1 = np.zeros(300)
plt.scatter(dist[:, 0], dist[:, 1])

mean2 = np.array([4.0, 5.0])
cov2 = np.array([[1.2, -0.4], [-0.4, 1.1]])

dist2 = np.random.multivariate_normal(mean2, cov2, 300)
print(dist2)
plt.scatter(dist2[:, 0], dist2[:, 1])
y2 = np.ones(300)
plt.show()

y = np.append(y1, y2, axis=0)
print(y) 
distfinal = np.append(dist, dist2, axis=0)
print(distfinal.shape)
df = pd.DataFrame(distfinal)
df2 = pd.DataFrame(y)
print(df.head())

df.to_csv('practices/x_values.csv', sep=',')
df2.to_csv('practices/y_values.csv', sep=',')


