import numpy as np
import matplotlib.pyplot as plt

import sys

sys.stdout = open("output.txt", "w")

mean_01 = np.array([-1, 0])
cov_01 = np.array([[1.2, 0.4], [0.4, 1.2]])

mean_02 = np.array([4, 5])
cov_02 = np.array([[1.2, 0.6], [0.6, 1.2]])

np.random.seed(3)
x1 = np.random.multivariate_normal(mean_01, cov_01, 500)
x2 = np.random.multivariate_normal(mean_02, cov_02, 500)

# plt.scatter(x1[:,0], x1[:,1])
# plt.scatter(x2[:,0], x2[:,1])
# plt.show()

data = np.zeros((1000, 3))

data[:500, :2] = x1
data[500:, :2] = x2
data[500:, -1] = 1

np.random.shuffle(data)
# print(data)

split = int(0.8 * data.shape[0])
xtrain = data[:split, :2]
ytrain = data[:split, -1]

xtest = data[split:, :2]
ytest = data[split:, -1]

# print(xtrain.shape)
# print(ytrain.shape)
# print(xtest.shape)
# print(ytest.shape)
# exit(1)
# plt.scatter(xtrain[:,0], xtrain[:,1], c=ytrain)
# plt.show()

# Normalization
xmean = xtrain.mean(axis=0)
xstd = xtrain.std(axis=0)
xtrain = (xtrain - xmean) / xstd

# print(xtrain.std(axis=0))
# print(xtrain.mean(axis=0))

# Normalized Visulization
# plt.scatter(xtrain[:, 0], xtrain[:, 1], c=ytrain)
# plt.show()

# test data should also be shifted by same mean as training data
xtest = (xtest - xmean) / xstd


# implementation of logistic regression
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def hypothesis(X, theta):
    """
    hypothesis = g(theta_Transpose_X)
    g() = 1 / 1 + e-theta_Transpose_X
    """
    y_ = sigmoid(np.dot(X, theta))
    return y_


# print(sigmoid(0))
# hh = np.linspace(-10, 10, 20)
# plt.plot(hh, sigmoid(hh))
# plt.show()


def error(X, Y, theta):
    """
    params :
    X — (m,n+l)
    theta — (n+l,l)
    return:
        scale value = loss
    """
    y_ = hypothesis(X, theta)
    # print(y_.shape)
    # print(Y.shape)
    # exit(1)
    L = -1 * np.mean(Y * np.log(y_) + (1 - Y) * np.log(1 - y_))
    return L


def gradient(X, Y, theta):
    m = X.shape[0]
    y_ = hypothesis(X, theta)
    # print(y_.shape)
    # print(X.shape)
    # print((Y - y_).shape)
    grad = -np.dot(X.T, (Y - y_))
    # print(grad.shape)
    return grad / m


def gradientDescent(X, Y, alpha=0.1, maxIters=300):
    n = X.shape[1]
    theta = np.zeros((n, 1))
    errorlist = []
    for i in range(maxIters):
        grad = gradient(X, Y, theta)
        # print(grad)
        # print(grad.shape)
        # print(theta.shape)
        e = error(X, Y, theta)
        # exit(1)
        errorlist.append(e)
        theta = theta - grad * alpha

    return theta, errorlist


ones = np.ones((xtrain.shape[0], 1))
xNewTrain = np.hstack((ones, xtrain))
ytrain = ytrain.reshape((-1, 1))
# print(xNewTrain.shape)
# exit(1)

theta, errorlist = gradientDescent(xNewTrain, ytrain)
print(theta)
print(theta.shape)
'''
[[0.00945452]
 [2.17121633]
 [2.11908669]]
'''
# plt.plot(errorlist)
# plt.show()



# draw line
# theta[0] + theta[1] * x1 + theta[2] * x2 = 0
# x2 = -(theta[0] / theta[2] + theta[1] / theta[2] * x1)

x1 = np.arange(-3, 4)
x2 = -(theta[0] / theta[2] + (theta[1] / theta[2]) * x1)

plt.scatter(xtrain[:, 0], xtrain[:, 1], c=ytrain.reshape((-1,)))
plt.plot(x1, x2)
plt.show()


# predictions
def predict(X, theta):
    h = hypothesis (X, theta)
    output = np. zeros(h.shape)
    output [h >= 0.5] = 1
    output = output. astype('int')
    # print(output)
    return output

ones = np.ones((xtest.shape[0], 1))
xNewTest = np.hstack((ones, xtest))
XT_preds = predict(xNewTrain, theta)
Xt_preds = predict(xNewTest, theta)


def accuracy(actual, preds):
    actual = actual.astype('int')
    actual = actual.reshape((-1, 1))
    acc = np.sum(actual == preds)/actual.shape[0]
    return acc*100

training_acc = accuracy(ytrain, XT_preds)
print(training_acc)
test_acc = accuracy(ytest, Xt_preds)
print(test_acc)
