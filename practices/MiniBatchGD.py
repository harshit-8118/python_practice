import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn import linear_model
from sklearn.datasets import make_regression

import sys
sys.stdout = open('output.txt', 'w')


X, Y = make_regression(n_samples=10000, n_features=20, n_informative=20, noise=20, random_state=1)

u = np.mean(X, axis=0)
std = np.std(X, axis=0)
# normalization
X = (X - u) / std
 
ones = np.ones((X.shape[0], 1))
X = np.hstack((ones, X))

# print(X.shape)
# print(Y.shape) 

def hypothesis(X, theta):
    return np.dot(X, theta)


def error(X, Y, theta):
    jtheta, m = 0.0, X.shape[0]
    y_ = hypothesis(X, theta)
    jtheta = np.sum((y_ - Y) ** 2)
    return jtheta / m

def gradient(X, Y, theta):
    m = X.shape[0]
    y_ = hypothesis(X, theta)
    grad = np.dot(X.T, (y_ - Y))
    return grad / m

# Batch gradient Descent
def gradientDescent(X, Y, alpha = 0.01, maxIters = 1000):
    n = X.shape[1] 
    theta = np.zeros((n, ))
    errorlist = []
    for i in range(maxIters):
        grad = gradient(X, Y, theta)
        e = error(X, Y, theta)
        errorlist.append(e)
        theta = theta - alpha * grad

    return theta, errorlist

theta, errlist = gradientDescent(X, Y)
print(theta, errlist[-1])
plt.plot(errlist)
plt.show()

# Mini Batch Gradient Descent
def MiniBGradientDescent(X, Y, batchSize = 200, alpha = 0.01, maxIters = 50):
    m, n = X.shape  
    theta = np.zeros((n, ))
    errorlist = []
    data = np.hstack((X, Y.reshape(-1, 1)))
    totalBatches = m // batchSize
    for i in range(maxIters):
        np.random.shuffle(data)
        for j in range(0, totalBatches):
            st, end = j * batchSize, j * batchSize + batchSize
            batchData = data[st:end, :]
            batchX = batchData[:, :-1]
            batchY = batchData[:, -1]
            batchGrad = gradient(batchX, batchY, theta)
            e = error(batchX, batchY, theta)
            errorlist.append(e)
            theta = theta - alpha * batchGrad

    return theta, errorlist


theta, errlist = MiniBGradientDescent(X, Y)
print(theta, errlist[-1])
plt.plot(errlist) # noisy
plt.show()