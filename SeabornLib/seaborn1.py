import seaborn as sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
sys.stdout = open('output.txt', 'w')

tips = sb.load_dataset('tips')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# print(tips)
# print(tips['sex'])
sb.set_theme()
# sb.barplot(x='sex', y='total_bill', data=tips)
# sb.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
# plt.show()

# sb.countplot(data=tips, x='sex')
# sb.countplot(x='time', data=tips)
# sb.countplot(x='day', data=tips)
# plt.show()

'''  boxplot helps us to generate outliers, quartiles   '''
# sb.boxplot(x='day', y='total_bill', data=tips, palette='dark:red', hue='smoker')
# sb.boxplot(x='day', y='total_bill', data=tips, palette='dark:red', hue='sex')
# plt.show()

# sb.violinplot(x='day', y='total_bill', data=tips, split=True, hue='sex')
# plt.show()

'''  distribution plot => shows us distribution of one variable  '''
# sb.distplot(tips['total_bill'], kde=False, bins=243)
# plt.show() 

# sb.kdeplot(tips['total_bill'])
# plt.show()

# sb.jointplot(data=tips, x='total_bill', y='tip')
# sb.jointplot(data=tips, x='total_bill', y='tip', kind='reg') # kind=hex, kde, scatter, reg
# plt.show()

# sb.pairplot(data=tips, hue='sex')
# plt.show()

# print(tips.head())
# tips = tips[['total_bill', 'size', 'tip']]
# print(tips)
# tips_corr = tips.corr()
# print(tips_corr)

'''  heat map :: should have varible's in both direction like correlation '''
# sb.heatmap(data=tips_corr, annot=True)
# plt.show()

'''  '''
flights = sb.load_dataset('flights')
# print(flights)

# flights_pivot = flights.pivot_table(index='month', columns='year', values='passengers')
# print(flights_pivot)

# sb.heatmap(data=flights_pivot)
# plt.show()

''' '''
titanic = sb.load_dataset('titanic')
titanic = titanic[['survived', 'pclass', 'age', 'fare']].corr()
print(titanic)

sb.heatmap(titanic, annot=True)
plt.show()






