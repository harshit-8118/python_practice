# 1
'''
1. install scrapy using command line
~ pip install scrapy

2. create project with command line
~ scrapy startproject "projectname"

3. there is a concept of crawling from web using "spiders"
- class inherits scrapy.Spider
- start_requests(self)[mandatory function] yields (url||urls) and calls callback()
- callback process further data

4. to run the scrapy file
~ scrapy crawl "file"
'''

# 2

"""
1. Parsing html Response from terminal 

~ scrapy shell "https://quotes.toscrape.com/page/1/"
We will recieve "response" in html

now, we can parse

~ response.css('title').getall()
~ response.css('title::text').getall()
~ response.css('title::text').getall()[0]
~ response.css('title::text').get()
~ response.css('div.quote::text').getall()
~ response.css('div.quote::text').get()
~ quote = response.css('div.quote')[0]
~ title = response.css('span.text').get()
~ print(title)
~ author = response.css('small.author').get()
~ print(author)
~ for q in response.css('div.quote"):
...:     text = q.css("span.text::text).get()
...:     print(text)
~ attr = response.css('li.next a::attr(href)').get()
~ attr = response.css('li.next a').attrib['href]

"""

# 3

'''
yielding crawled content in json format in shell
~ scrapy crawl quotes_spider -o quotes.json


'''