import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json?'

parameters = {
    'address': "coding blocks pitampura",
    'key': "AizaSyDxpzAOiOie21qiUffhWegOvmbKH25TNIE"
}

try:
    r = requests.get(url, parameters)
except:
    print('failed')
else:
    print(r.url)
    print(r.content)
finally:
    print('over')






