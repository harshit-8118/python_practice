import requests
import json

url = 'https://www.googleapis.com/customsearch/v1?'

parameters = {
    'q': "coding blocks pitampura",
    'key': "AIzaSyDye6WKCdUXMgCCYNw3zvkAIuSEoyLWlq4",
    "cx":"d43b1771893534bf5"
}

try:
    r = requests.get(url, parameters)
except:
    print('failed')
else:
    print(r.url)
    d = json.loads(r.content)
    # print(d)
    with open('WEB_SCRAPING\p2\google_json.json', 'w', encoding='utf-8') as F:
        ff = json.dumps(d)
        F.write(ff)
finally:
    print('over')






