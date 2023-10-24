from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import sys
sys.stdout = open('output.txt', 'w')
#read csv file

df = pd.read_csv('Matplot\movie_metadata.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# print(df.columns)
# df= df.loc[:, df.columns]
# print(df)
# print(df.head())
# df = df.iloc[:, 1:-1] # slicing records
df = df.loc[:, ['Movie']]
# df = df.get('Movie')
# print(df)

titles = dict()
for i in df.Movie:
    length = len(i)
    if length in titles:
        titles[length] += 1
    else: titles[length] = 1

# print(titles)

X = np.array(list(titles.keys()))
Y = np.array(list(titles.values()))

plt.scatter(X, Y, color='green', label='no of movies')
plt.xlabel('Length of movies')
plt.ylabel('no of movies')
plt.ylim(-5, 20)
plt.xlim(-5, 70)
plt.legend()
# plt.show()




























