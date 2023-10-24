import numpy as np
import matplotlib.pyplot as plt

import sys
sys.stdout = open('output.txt', 'w')

# mat = np.ones((5, 5, 3), dtype='int32')

# mat[:3, :, 0] = 100
# mat[3:, :, 1] = 100

# plt.imshow(mat)
# plt.show()

np.random.seed(1)
a = np.random.randint(5, 10, (10, 5, 3))
# print(a)
# print(np.transpose(a, axes=(2, 1, 0))) # default
# print(np.transpose(a, axes=(0, 2, 1)))

# print(a[0][0])

''' element-wise multiplication/ dot-product or mat multiplication '''
x = np.array([[1, 2, 3], [4, 5, 6], [2, 5, 6]])
y = np.array([[2, 3, 4], [5, 6, 7], [1, 3, 4]])

# print(x * y)

# print(np.dot(x, y))
# print(x.__matmul__(y))
# print(x.dot(y))

from numpy import linalg as lg
import math
a = [-3, 4]

# print(lg.norm(a)) # L2 or eigen value 
# print(math.cbrt(3**3 + 4**3)) # L3
# # or
# print(lg.norm(a, ord=(3))) 

# print(lg.norm(a, ord=1)) # L1
# print(lg.norm(a, ord=10)) # L10

# print(lg.norm(x)) # matrix norm
# print(lg.norm(a, ord=np.inf)) # max norm Linf

# print(lg.det(x))
# inv = lg.inv(x)
# print(inv)
# print(x.dot(inv))


A = np.array([[2, 3], [4, 6]])

print(lg.det(A))
# print(lg.inv(A)) # error As det(A) == 0

print(lg.pinv(A))


''' solve Ax = B '''
A = np.array([[2, 3], [3, 1]])
B = np.array([8, 5])
''' x  = A^-1.B   '''
print(lg.inv(A).dot(B))
# or 
print(lg.solve(A, B))