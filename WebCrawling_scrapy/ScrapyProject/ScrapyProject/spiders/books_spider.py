from typing import Any, Iterable
import scrapy, json

import sys
sys.stdout = open('output.txt', 'w')

class books_spider(scrapy.Spider):
    name = 'books_spider'

    def start_requests(self):
        uri = 'https://www.junkybooks.com/books?page=1'
        yield scrapy.Request(url=uri, callback=self.parse)

    def parse(self, response) -> Any:
        page_no = response.url.split('?page=')[-1]
        # print(page_no, type(page_no))
        
        books = dict()        

        for (i, q) in enumerate(response.css('div.product-wrapper')):
            img_url = 'https://www.junkybooks.com/' + q.css('a > img.primary::attr(src)').extract()[0]
            book_name = q.css('h4 > a::text').extract()[0]

            books[i] = {
                'book_img' : img_url,
                'book_name': book_name,
            }

        filename = 'BookRecords/books-{}.json'.format(page_no)
        # print(books)
        # print(filename)

        
        with open(filename, 'w') as f:
            f.write(json.dumps(books)) 

        for page in range(int(page_no) + 1, 10):
            next_url = response.url[:-1] + str(page)
            # print(next_url)
            yield scrapy.Request(url=next_url, callback=self.parse)


