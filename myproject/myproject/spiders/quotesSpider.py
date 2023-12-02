from typing import Iterable
import scrapy
from scrapy.http import Request, Response
import json

class quotesSpider(scrapy.Spider):
    name = "quotesSpider"

    def start_requests(self) -> Iterable[Request]:
        urls = [
            'https://quotes.toscrape.com/page/1/',
            # 'https://quotes.toscrape.com/page/2/',
            # 'https://quotes.toscrape.com/page/3/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response: Response):
        page_id = response.url.split('/')[-2]
        filename = "quotes-%s.html"%page_id
        with open(filename, 'wb') as ff:
            ff.write(response.body)
        quotes = response.css('div.quote')
        qt = []
        for quote in quotes:
            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('a.tag::text').getall()
            d = {
                'text':text[1:-1],
                'author':author,
                'tags':tags
            }
            qt.append(d)
            
        with open('quotes-%s.json'%page_id, 'w') as f:
            ct = json.dump(qt, f)
        
        next_page = response.css('li.next a').attrib['href']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
        