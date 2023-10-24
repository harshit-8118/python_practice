
# Surface Plots I Data Visualisation
# urface Plots are used to
# - Visualise Loss Functions in Machine Learning & Deep Learning
# - Visualise State or State Value Functions in Reinforcement Learning

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a = np.array([1, 2, 3])
b = np.array([4, 5, 6, 7])
 

# meshgrid makes two arrays of same dimension, a's row_number = b's size and b's coloumn_number = a's size
a, b = np.meshgrid(a, b)
# print(a, b)
'''
a = [[1 2 3]
 [1 2 3]
 [1 2 3]
 [1 2 3]] 
b = [[4 4 4]
 [5 5 5]
 [6 6 6]
 [7 7 7]]
'''

a = np.arange(-1, 1, 0.02)
b = a

a, b = np.meshgrid(a, b)

fig = plt.figure()
axes = fig.add_subplot(111, projection='3d')
axes.plot_surface(a, b, a**2+b**2, cmap='rainbow')
plt.show()

fig = plt.figure()
axes = fig.add_subplot(111, projection='3d')
axes.contour(a, b, a**2 + b**2, cmap='rainbow')
plt.show()

