import matplotlib.pyplot as plt
import numpy as np

import sys
sys.stdout = open('output.txt', 'w') 


x = np.arange(0, 10, 0.3)
# print(x)

y = x**2
# print(type(y))
# y = [float(x) for x in y]
# print(y)
y = [round(float(x), 3) for x in y]
# print(y)
y = np.array(y)
# print(type(y))
y2 = 2 * x + 3

# print(plt.style.available)
plt.style.use('seaborn-v0_8-paper')

# plt.plot(x, y)
# plt.grid(True)
# plt.xlabel('x-vals')
# plt.ylabel('y-vals')
# plt.title('f(x)->[x**2, 2*x + 2]')
# plt.plot(x, y, color='red', label='y[x**2]', marker='^')
# plt.plot(x, y2, color='green', label='y2[2*x + 3]', linestyle='dashed')
# plt.legend()
# plt.show()



# prices = np.array(np.arange(6)) ** 4
# plt.plot(prices)      # price will be plotted on y-axis taking x-axis len(prices)
# plt.show()


''' scatter-plot'''
 
# plt.figure(figsize=(10,4)) # 10 cols, 4 rows
# plt.grid(True)
# plt.scatter(x, y, marker='^', color='red', label='large house')
# plt.scatter(x, y2, marker='*', color='blue', label='small houses')
# plt.xlabel('area')
# plt.ylabel('prices')
# plt.title('House prices')
# plt.legend()
# plt.show()

''' BAR graphs '''

# plt.style.use('dark_background')
# x_cord = np.array([0, 1, 2])*1.1
# plt.bar(x_cord, [10, 20, 14], label='old prices', width=0.6, tick_label=['Gold', 'Platinum', 'Silver']) # first year prices
# plt.bar(x_cord + 0.4, [20, 10, 8], label='new prices', width=0.4) # second year prices
# plt.legend()
# plt.title('Metal Price Comparision')
# plt.xlabel('Metal')
# plt.ylabel('Price') 
# plt.ylim(-5, 30)
# plt.show()


''' Pie chart '''
# sub = ['Maths', "English", 'Physics', 'Chem']
# weightage = [20, 10, 15, 15]
# plt.pie(weightage, labels=sub, explode=[0.05,0,0.4,0], autopct='%1.2f%%', shadow=True, startangle=90)
# plt.show()

''' Histogram '''
# np.random.seed(3)
Xsn = np.random.randn(100)  # values generated => Standard Normal Distribution
Miu = 60
sigma = 5
# formulae is :: Xsn = (X - Miu) / sigma
X = np.round(Xsn * sigma + Miu)
X2 = np.round(Xsn * 8 + 40)
# print(X) 

plt.hist(X, align='left', alpha=0.8, label='Maths')
plt.hist(X2, alpha=0.8, label='Physics')
''' we can see most of the values lies in between 
55-65 as mean is 60 and standard deviation in 5.

we had standard normal distribution from randn function 
'''
# print(X)
# d = {}
# for i in sorted(X):
#     if i in d:
#         d[i] += 1
#     else: d[i] = 1
# print(d) 

plt.title('Histogram')
plt.xlabel('Marks')
plt.ylabel('Prob/freq count of students')
plt.legend()
plt.show()




