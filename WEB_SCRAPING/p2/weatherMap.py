from urllib.request import urlopen
import json

import sys
sys.stdin = open('p2/input.txt', 'r')
sys.stdout = open('p2/output.txt', 'w')


api_url = 'http://api.weatherapi.com/v1/search.json?key=47aee95526ea4fcd985165554232609&q=London'

url_result = urlopen(api_url)
# print(url_result.read())

data = url_result.read()
json_data = json.loads(data)

# print(type(json_data)) # list
print(json_data[0])
print(json_data[0]['name'])

with open('p2/weather.json', 'w') as w:
    w.write(json.dumps(json_data)) 
    