import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import sys
sys.stdout = open('output.txt', 'w')

dfx = pd.read_csv('practices/x_values.csv')
dfy = pd.read_csv('practices/y_values.csv')

# print(dfx.head())
X = dfx.values
Y = dfy.values
X = X[:, 1:]
Y = Y[:, 1]
# print(X)
# print(Y)

plt.scatter(X[:, 0], X[:, 1], c=Y)
point = np.array([2.1, 3.6])

plt.scatter(point[0], point[1], c='red')
plt.show()

def eucledian(X1, X2):
    return np.sqrt(sum((X1 - X2)**2))

def knn(X, Y, query_point, k = 5):
    m = X.shape[0]
    dists = []
    for i in range(m):
        dist = eucledian(X[i], query_point)
        dists.append((dist, Y[i]))

    dists = sorted(dists)[:k]
    topklabels = [i[1] for i in dists]
    labels, counts = np.unique(topklabels, return_counts=True)
    cluster = labels[np.argmax(counts)]
    print('Cluster belongings: ', cluster)
    return dists

vals = knn(X, Y, point)
vals = knn(X, Y, [0, 2])
vals = knn(X, Y, [4, 5])
print(vals)

