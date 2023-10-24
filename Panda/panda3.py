import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.stdout = open('output.txt', 'w')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('Panda/movie_metadata.csv').drop(columns=['Unnamed: 5'])
# print(df)

movies = df['Movie']
data = dict()
for i in movies:
    if len(i) in data:
        data[len(i)] += 1
    else: data[len(i)] = 1

# print(data)
X = data.keys()
Y = data.values()

print(X, Y)
plt.scatter(X, Y, c='red', alpha=0.8)
plt.xlabel('movie length')
plt.ylabel('no. of movies')
plt.show()
