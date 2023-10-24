import numpy as np
import matplotlib.pyplot as plt

X = np.arange(11)
Y = (X - 5 ) ** 2

print(X, Y)

# print(plt.style.available)
plt.style.use('seaborn-v0_8')
# plt.xlim(-5, 25)
# plt.ylim(-5, 30)

plt.plot(X, Y)
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.show()

x = 50
step = 0.1

error = []
for i in range(50):
    grad = 2 * (x - 5)
    x = x - step * grad
    e = (x - 5) ** 2
    plt.scatter(x, e)
    error.append(e)

plt.show()
plt.plot(error)
plt.show()




