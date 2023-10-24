from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

import sys
sys.stdout = open('p1/Soup.html', 'w', encoding='utf-8')

android_url = 'https://en.wikipedia.org/wiki/Android_version_history'

try:
    android_data = urlopen(android_url)
    android_html = android_data.read()
    # print(type(android_data))
    # print(android_html)
    android_data.close()
except Exception as e:
    print(e)
    sys.exit(1)

android_soup = soup(android_html, 'html.parser', from_encoding='utf-8')
# print(type(android_soup))

# print(android_soup.h1)
# print(android_soup.findAll('h1', {}))

android_table = android_soup.findAll('table', {'class':'wikitable'})[0]
# print(android_table)

table_header = android_table.findAll('th')
# print(table_header)

''' table columns name as (a list) '''
column_titles = [th.text[:-1] for th in table_header]
# print(column_titles)
''' or '''
# for th in table_header:
#     print(th.text[:-1])

rows_data = android_table.findAll('tr', {})[1:-1]
# print(len(rows_data))
# print(rows_data[0])
''' for single row '''
# first_row =  rows_data[0].findAll('td')
# for d in first_row:
#     print(d.text[:-1])

table_rows = []
for row in rows_data:
    curr_row = []
    row_data = row.findAll('td')
    if len(row_data) <= 4:
        continue
    for idx, data in enumerate(row_data):
        if idx == 2 or data.text.find(": ") != -1:
            curr_row.append(data.text[:-1].split(': ')[-1])
        else:
            curr_row.append(data.text[:-1])
    table_rows.append(curr_row)
 
# print(table_rows)

filename = 'p1/android_version_history.csv'

with open(filename, 'w', encoding='utf-8') as csvfile:
    '''  write header '''
    header_string = ",".join(column_titles)
    header_string += '\n'
    # print(header_string)
    csvfile.write(header_string)
    ''' write rows '''
    for row in table_rows:
        row = [i.replace(",", "") for i in row]
        row_string = ", ".join(row)
        row_string += '\n'
        csvfile.write(row_string) 

df = pd.read_csv(filename)

df.fillna("-", inplace=True)
pd.set_option('display.max_columns', None)

print(df.head(n=36))
# print(df.iloc[1][1])                




