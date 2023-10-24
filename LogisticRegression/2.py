import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_regression

import sys
sys.stdout = open('output.txt', 'w')


mean1 = np.array([-1, 0])
cov1 = np.array([[1.2, 0.4], [0.4, 1.2]])

mean2 = np.array([4, 5])
cov2 = np.array([[1.2, 0.6], [0.6, 1.2]])

np.random.seed(3)
c0 = np.random.multivariate_normal(mean1, cov1, 500)
c1 = np.random.multivariate_normal(mean2, cov2, 500)

data = np.zeros((1000, 3))

data[:500, : 2] = c0
data[500:, : 2] = c1
data[500:, -1] = 1

# print(data)
np.random.shuffle(data)

split = int(0.8 * data.shape[0])
xtrain = data[:split, :2]
ytrain = data[:split, -1]

xtest = data[split:, :2]
ytest = data[split:, -1]

'''==== Need not to do this computation ===='''
# ones = np.ones((xtrain.shape[0], 1))
# xtrain = np.hstack((ones, xtrain))

# ones = np.ones((xtest.shape[0], 1))
# xtest = np.hstack((ones, xtest))
# ytrain = ytrain.reshape((-1, 1))
# ytest = ytest.reshape((-1, 1))

# print(xtest.shape)
# print(xtrain.shape)
# print(ytest.shape)
# print(ytrain.shape)

model = LogisticRegression()
model.fit(xtrain, ytrain)
theta0 = model.intercept_
theta_s = model.coef_

print(theta0, theta_s)
print(model.score(xtrain, ytrain))
print(model.score(xtest, ytest))


ypred = model.predict(xtest)
print(ypred.shape)
