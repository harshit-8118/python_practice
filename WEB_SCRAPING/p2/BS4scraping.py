import bs4
import requests
url = 'https://www.passiton.com/inspirational-quotes?page=2'

response = requests.get(url)

soup = bs4.BeautifulSoup(response.content, 'html.parser')
# print(soup)

img_div = soup.findAll('div', {'class':"col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top"})
# print(img_div)

img_urls = []

for div in img_div:
    d = div.find('img')
    # print(d.attrs)
    img_urls.append(d.attrs['src'])

# print(img_urls)

for i, uris in enumerate(img_urls):
    with open('p2/img/inspiration{}.jpg'.format(i), 'wb') as file:
        img = requests.get(uris)
        file.write(img.content)




