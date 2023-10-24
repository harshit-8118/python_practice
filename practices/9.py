from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from sklearn import linear_model
import numpy as np
import pandas as pd

import sys
sys.stdout = open('output.txt', 'w')

X = pd.read_csv('LinearRegression\X_train.csv')
Y = pd.read_csv('LinearRegression\Y_train.csv')


X = X.values
Y = Y.values[:, -1]

# print(X.shape)
# print(Y.shape)
# print(X, Y)
# exit(1)

# normalize
mean = X.mean()
std = X.std()
X = (X - mean) / std
ones = np.ones((X.shape[0], 1))
X = np.concatenate((ones, X), axis=1)

# print(X, Y)
# plt.scatter(X, Y)
# plt.show()

def hypothesis(x, theta):
    return np.dot(x, theta)


def error(X, Y, theta):
    m = X.shape[0]
    y_ = hypothesis(X, theta)
    jtheta = np.sum((y_ - Y) ** 2)

    return jtheta / m


def gradient(X, Y, theta):
    m = X.shape[0]
    y_ = hypothesis(X, theta)
    grad = np.dot(X.T, (y_ - Y))

    return grad / m


def gradient_descent(X, Y, learning_rate=0.1, max_epochs=300):
    n = X.shape[1]
    theta = np.zeros((n,))

    errorlist = []
    for i in range(max_epochs):
        e = error(X, Y, theta)
        errorlist.append(e)
        grad = gradient(X, Y, theta)
        theta = np.subtract(theta, learning_rate * grad)

    return theta, errorlist


theta, errorlist = gradient_descent(X, Y)

X_test = pd.read_csv('LinearRegression\X_test.csv')
X_test = X_test.values
ones = np.ones((X_test.shape[0], 1))
X_test = np.concatenate((ones, X_test), axis=1)
y_ = hypothesis(X_test, theta)
print(y_)

plt.plot(errorlist)
plt.show()