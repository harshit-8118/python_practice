from typing import Any, Iterable
import scrapy
from scrapy.http import Request, Response
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider" # this should be same as file name and mandatory

    def start_requests(self) -> Iterable[Request]:

        urls = [
            'https://quotes.toscrape.com/page/1/',
            # 'https://quotes.toscrape.com/page/2/',
            # 'https://quotes.toscrape.com/page/3/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response: Response) -> Any:
        page_id = response.url.split('/')[-2]

        # filename = "ResponsesQuotes/quotes-%s.html"%page_id
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        
        # self.log('saved file {}'.format(filename))
        
        quotes = dict()
        for i, q in enumerate(response.css('div.quote')):
            text = q.css('span.text::text').get()
            author = q.css('small.author::text').get()
            tags = q.css('a.tag::text').getall()
            
            # yield {
            #     'text': text[1:-1],
            #     'author': author,
            #     'tags': tags
            # }

            # or

            quotes[i] = {
                'text': text[1:-1],
                'author': author,
                'tags': tags
            }
        
        quotes_json_file = "ResponsesQuotes/quotes-" + page_id + '.json'
        with open(quotes_json_file, 'w') as f:
            jj = json.dumps(quotes)
            # print(jj)
            # print(type(jj))
            f.write(jj)

        # Recursive calling through paging method...
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print('next page is ::: ',next_page)
            yield scrapy.Request(next_page, callback=self.parse)



        
