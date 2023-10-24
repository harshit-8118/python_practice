import requests

url = 'https://graph.facebook.com/4/picture?type=large'

r = requests.get(url)
# print(r.content)

with open('p2/fbimage.jpg', 'wb') as f:
    f.write(r.content)