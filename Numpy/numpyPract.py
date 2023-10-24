import numpy as np

''' Basic '''
# a = np.array([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]])
# print(type(a))
# print(a.shape)
# print(a.transpose())
# print(a)
# print(a.__matmul__(a.transpose()))
# print(*a)
# c = np.array([
#     [1, 2, 3], [4, 5, 6]
# ])
# print(c.shape)
# print(c)

''' create array of zeros, ones ''' 

# z = np.zeros((2, 3))
# print(z)
# z = np.zeros((5, 3))
# z[:, 1] = 1
# z[2, :] = 2
# print(z)
# o = np.ones((2, 3, 5), int)
# print(o)

''' array of constants '''
# c = np.full((5, 4, 2), 5)
# print(c)


''' identity matrix '''
# idenMat = np.eye(3)
# print(idenMat)
# idenMat = np.eye(5, 4) # default shift = 0
# print(idenMat)
# idenMat = np.eye(5, 4, 1) 
# print(idenMat)
# idenMat = np.eye(5, 4, 1, str) 
# print(idenMat)

''' random matrix '''
# randomMatrix = np.random.random((4, 3))
# print(randomMatrix)
# print(randomMatrix[:1])
# print(randomMatrix[:, 1])
# # randomMatrix[rowrange, colrange]   
# print(randomMatrix[1:3, 1:3])
# randomMatrix[2, 1:] =  1
# print(randomMatrix)

'''  datatype '''
# print(z.dtype)

''' mathematical operation '''
x = np.array([[1, 2], [3, 5]])
y = np.array([[5, 2], [5, 2]])
z = np.array([[6, 2], [5, 2]])
w = np.array([[5, 2], [5, 2]])

# print(x + y)
''' or '''
# print(x + y + z + w)
''' or '''
# print(x.__add__(y).__add__(z).__add__(w))
''' or '''
# print(np.add(x, y).__add__(z).__add__(w))
# print(np.subtract(z, w))
# print(z - w)
# print(z.__mul__(y))
# print(np.multiply(z, y))
# print(z.__divmod__(y))
# print(np.divide(z, y))
# print(np.divmod(z, y))

# print(np.sqrt(x))

'''  Matrix multiplication & dot products  '''
# print(x)
# print(y)

# print(x*y) 
# print(x.dot(y))
# print(np.dot(x, y))
# print(np.cross(x, y))

# there is difference between dot product and matrix multiplication 
'''
A = [[a1, a2], [a3, a4]], B = [[b1, b2], [b3, b4]] 
A.B = [[a1b1 + a2b3, a1b2 + a1b4], [a3b1 + a4b3, a3b2 + a3b4]]
A*B = [[a1b1, a2b2], [a3b3, a4b4]]
AxB = []
'''

a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
# print(a*b) # will return matrix 
# print(a.dot(b)) # will return scaler product || dot product
# print(sum(a))
# print(np.sum(x))
# print(np.sum(x, axis=1))
# print(np.sum(x, axis=0))

''' stack '''
print(a)
print(b)
b = b * 2
print(np.stack((a, b), axis=0))
print(np.stack((a, b), axis=1))
print(np.stack((x, y), axis=0))
print(np.stack((x, y), axis=1))

