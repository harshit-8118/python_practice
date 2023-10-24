import pandas as pd
import numpy as np

import sys
sys.stdout = open('output.txt', 'w')

'''
special object to data in tabular data(rows&cols)
'''

user_data = {
    "marksA": np.random.randint(1, 100, 10),
    "marksB": np.random.randint(50, 100, 10),
    "marksC": np.random.randint(1, 100, 10),
    "marksD": np.random.randint(75, 100, 10),
}

# print(user_data)
'''  change data in real numbers, by dtype= '''
df = pd.DataFrame(user_data, dtype='float32') 
# print(df) # table will be obtained
# print(df.head()) 
# print(df.columns)

df.to_csv('Panda/marks.csv')
csv = pd.read_csv('Panda/marks.csv')
csv = csv.drop(columns=['Unnamed: 0'])
print(csv)

''' gives statistics about data '''
# print(csv.describe())
'''
          marksA     marksB     marksC     marksD
count  10.000000  10.000000  10.000000  10.000000
mean   59.800000  71.200000  59.100000  90.100000
std    35.304391  14.053865  27.274123   7.752419
min     1.000000  57.000000  17.000000  77.000000
25%    31.750000  60.750000  37.500000  85.500000
50%    69.500000  67.000000  56.500000  91.500000
75%    85.750000  77.000000  81.250000  96.250000
max    97.000000  96.000000  98.000000  99.000000
'''

''' first 5 rows '''
# print(csv.head()) 
''' last 5 rows '''
# print(csv.tail())

''' access a row '''
row = csv.iloc[2, :]
# print(row)

# print(csv.columns)
idx = csv.columns.get_loc(key='marksC')
# print(csv.iloc[3, idx])

''' sort dataframe '''
# print(csv.sort_values(by=['marksC', 'marksA'], ascending=False))

''' return data in form of array  '''
csvarr = csv.values

print(csvarr, type(csvarr))

''' back to dataframe from numpy array '''
new_csv = pd.DataFrame(csvarr, columns=['Physics', 'Chemistry', 'Maths', 'Bio'])
# print(new_csv)

new_csv.to_csv('Panda/marks2.csv', index=False)
read_new_csv = pd.read_csv('Panda/marks2.csv')
print(read_new_csv.head())



