import numpy as np

''' arrange function in numpy'''
# b = np.arange(10)
# print(b)
# b = np.arange(2, 10)
# print(b)
# b = np.arange(2, 10, 2)
# print(b)


a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(np.random.random((3, 2)))

np.random.shuffle(a)
# print(a)

print(np.random.rand(2))
''' returns values from a Standard Normal Distribution '''
print(np.random.randn(2, 3))

print(np.random.randint(5, 8))
print(np.random.randint(5, 9, (4, 5)))
print(np.random.randint([3, 5, 3], 10, (5, 3)))
print(np.random.randint(5, [8, 10], size=(6, 2)))
print(np.random.randint([[3, 2, 5], [5, 3, 7]], [[10], [20]], size=(2, 3)))

print(np.random.choice([3, 4, 2, 5, 7]))

np.random.seed(1)
a = np.random.randint(2, 43, (4, 5))
print(a)
a.resize(2, 10) # returns None
print(a)
