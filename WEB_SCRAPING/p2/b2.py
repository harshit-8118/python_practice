from bs4 import BeautifulSoup as bs
import pandas
from urllib.request import urlopen

data = urlopen('https://www.passiton.com/inspirational-quotes?page=2')
html = data.read()

html = bs(html, 'html.parser')

Outerdivs = html.findAll('div', {'id': 'all_quotes'})[0]
divs = Outerdivs.findAll("div")
img_rows = []
for d in divs:
    img = d.find('img')
    img_rows.append(img.attrs['src'])


for i, img in enumerate(img_rows):
    d = urlopen(img).read()
    with open('WEB_SCRAPING/p2/bImgs/inspirational{}.jpg'.format(i+1), 'wb') as ff:
        ff.write(d)