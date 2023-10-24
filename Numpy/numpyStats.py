import numpy as np

np.random.seed(1)
a = np.random.randint(5, 99, size=(2, 4))
# print(a)
# print(np.min(a))

''' specify axis for the direction in case of multi-dimensional array '''
# print(np.min(a, axis=0))
# print(np.min(a, axis=1))

''' printing mean of arr '''
# print(np.size(a))
# m = np.sum(a) / np.size(a)
# print(m)

''' or '''
# print(np.mean(a))
# print(np.mean(a, axis=0))

# print(np.median(a))
''' or '''
# a = a.flatten()
# a = np.sort(a)
# print(a, type(a))
# print(a[len(a) // 2] if len(a) % 2 else (a[len(a) // 2] + a[(len(a) // 2) - 1]) / 2)

w = np.array([4, 2, 5, 6, 12])
print(np.mean(w))
print(np.average(w))
''' standard deviation o- = sqrt(1/N * sigma(Xi - u)^2)'''
print(np.std(w))
''' or '''
print(np.sqrt(np.mean(np.abs(w - np.mean(w)) ** 2)))
 
''' variance '''
print(np.var(w))
print(np.std(w) ** 2)