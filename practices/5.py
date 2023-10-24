import numpy as np
from matplotlib import pyplot as plt

import sys
sys.stdout = open('output.txt', 'w')


# standard normal distribution given by
miu = 0
sigma = 1

miu = 5
sigma = 2

# formula => u = (x - miu) / sigma
vals =  (miu + sigma * np.random.randn(1000))

# print(vals.shape)
# print(vals)

# print(np.mean(vals))
# print(vals.std())


'''testing with integer variables'''
# newvals = np.round(vals)
# z = np.unique(newvals, return_counts=True)
# print(z)
# print(newvals.mean())
# print(newvals.std())
''' testing end '''


# plt.hist(vals, bins=1000)
# plt.show()

x = vals[:200]
y = np.zeros(x.shape)
# will be observe density will be more near mean
# plt.scatter(x, y)
# plt.show()

''' Multivariate Normal Distribution '''

mean = np.array([0.0, 0.0])
cov = np.array([[1, 0], [0, 1]])

dist = np.random.multivariate_normal(mean, cov, 500)
print(dist.shape)

plt.scatter(dist[:, 0], dist[:, 1])
# plt.show()

mean2 = np.array([0.0, 0.0])
cov2 = np.array([[1, 0.8], [0.8, 1]])

mean2 = np.array([0.0, 0.0])
cov2 = np.array([[1, 0.5], [0.5, 1]])

mean2 = np.array([5.0, 6.0])
cov2 = np.array([[1.3, 0.2], [0.2, 1.1]])

dist2 = np.random.multivariate_normal(mean2, cov2, 500)

plt.scatter(dist2[:, 0], dist2[:, 1])
plt.show()

