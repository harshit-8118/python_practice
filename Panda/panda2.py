import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split as tst

import sys
sys.stdout = open('output.txt', 'w')
'''
Practice from MNIST dataset
'''
csv = pd.read_csv('Panda/mnist_train.csv')

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

# print(csv.shape)
# print(csv.head()) # [5 rows x 785 columns] flatten 28 * 28 matrix == 785 columns

data = csv.values
np.random.shuffle(data)
# print(data) 

# print(data.shape)

"separting label-image[Y] and data-image[X]"
X = data[:,1:]
Y = data[:, 0]
'''
Y    X-----------X
5    0 0 ... 0 0 0
0    0 0 ... 0 0 0
4    0 0 ... 0 0 0
............
5    0 0 ... 0 0 0
6    0 0 ... 0 0 0
8    0 0 ... 0 0 0
'''
# print(Y, Y.shape)   # label Y, to which corresponding image exists in X's row
# print(X, X.shape)   # X's single row is an image for label Y

# print(X[0]) 

''' 
####### start ##########
Visualize image 
show first 10 images from data-set in matplot
'''
def drawImg(X, Y, i):
    plt.figure(figsize=(3,2))
    plt.imshow(X[i].reshape(28, 28), cmap='gray')
    plt.title('Label: ' + str(Y[i]))
    plt.show()

# for i in range(5):
#     drawImg(X, Y, i)
''' 
####### end ##########
'''

'''
How to test data ?,
we must have large training set and around 1/4th test data.
split test set from training data with ratio [80% training / 20% test] data.
// can also use sklearn library to split data into test and training data 
# must randomly shuffled data => we can't do shuffling on X, Y we should do shuffling on data array
'''

print(type(X))
split = int(0.8 * X.shape[0])
X_train = X[: split, :]
Y_train = Y[: split]

X_test = X[split:, :]
Y_test = Y[split:]

# print(type(X_train), type(X_test))
# print(X_train.shape)
# print(Y_train.shape)
# print(X_test.shape)
# print(Y_test.shape)
'''
(48000, 784)
(48000,)
(12000, 784)
(12000,)
'''

# Try to plot a visualization (Grid of first 25 images)
# plt.figure(figsize=(10, 15))
# for i in range(25):
#     plt.subplot(5,5, i + 1)
#     plt.imshow(X_train[i].reshape(28, 28), cmap='gray', aspect=3/5) # aspect=height/width
#     plt.title("Label: " + str(Y_train[i]))
#     plt.axis('off')
# plt.show()

# Xtrain, Xtest, Ytrain, Ytest = tst(X, Y, train_size=0.8, random_state=5)
# print(Xtrain.shape)
# print(Ytrain.shape)
# print(Xtest.shape)
# print(Ytest.shape)













































