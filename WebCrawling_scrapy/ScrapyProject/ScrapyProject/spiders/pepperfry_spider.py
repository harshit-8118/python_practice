import scrapy, json, os, re, requests
from scrapy.http import HtmlResponse
from scrapy.pipelines.images import ImagesPipeline

import sys
sys.stdout = open('output.txt', 'w')

class PepperFry(scrapy.Spider):
    name = 'pepperfry_spider'
    base_dir = 'PepperFryData/'
    MaxCnt = 20

    def start_requests(self):
        base_url = 'https://www.pepperfry.com/site_product/search?q='

        # items = ['two seater sofa', 'bench', 'book cases', 'coffee', 'table', 'dining set', 'queen beds', 'arm chairs', 'chest drawers', 'garden seating', 'bean bags', 'king beds']
        items = ['two seater sofa']

        urls = []
        dir_names = []
        for item in items:
            query_string = '+'.join(item.split(' '))
            dir_name = '-'.join(item.split(' '))
            dir_names.append(dir_name)
            urls.append(base_url + query_string)

            dir_path = self.base_dir + dir_name
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

        # print(urls)
        # print(dir_names)

        for i in range(len(urls)):
            d = {
                'dir_name': dir_names[i]
            }
            resp = scrapy.Request(url=urls[i], callback=self.parse, dont_filter=True)
            resp.meta['dir_name'] = dir_names[i]
            yield resp



    def parse(self, response, **meta):
        # response.selector.xpath('').extract()
        # products_urls = response.xpath('//div/div/div/a[@p=0]/@href').extract()
        products_urls = response.css('div.product-card-image > a::attr(href)').extract()
        # print(len(products_urls))

        products_urls = ['https://www.pepperfry.com' + w for w in products_urls]
        print(products_urls)
        counter = 0

        for url in products_urls[:1]:
            resp = scrapy.Request(url=url, callback=self.parse_item, dont_filter=True)
            # print(resp)
            resp.meta['dir_name'] = response.meta['dir_name']

            if counter == self.MaxCnt:
                break

            if not resp == None:
                counter += 1
                # print(resp)
            yield resp
    

    def parse_item(self, response, **meta):
        item_title = response.css('div.vip-share-name-container > h1::text').extract()[0][:-1]
        # print(item_title)
        item_price = response.xpath('//div/div/div/p/b[@class="pf-orange-color pf-large font-20 pf-primary-color"]/text()').extract()[0].strip()
        # print(item_price) 

        item_savings = response.xpath('//p[@class="pf-margin-0 pf-bold-txt font-13"]/text()').extract()[0].strip()
        item_description = response.xpath('//div[@itemprop="description"]/div/p/text()').extract()

        item_details_keys = response.xpath('//div[@id="itemDetail"]/p/b/text()').extract()
        item_details_values = response.xpath('//div[@id="itemDetail"]/p/text()').extract()

        brand = response.xpath('//span[@itemprop="brand"]/text()').extract()
        item_details_values[0] = brand[0]
        
        stop_words = ["(all dimensions in inches)", "(all dimensions in inches)", "(all dimensions in inches)"]

        item_details_values = [word.strip() for word in item_details_values if word not in stop_words]

        a = len(item_details_keys)
        b = len(item_details_values)
        idetail = {}

        for i in range(min(a, b)):
            idetail[item_details_keys[i]] = item_details_values[i]

        # print(idetail)
        
        # print(item_details_keys)
        # print(item_details_values)

        stop_items = ['pepperfry.com', 'We also offer you a', 'So go ahead and buy with confidence.', 'Brand will upfront contact you for assembly']

        item_description = filter(lambda x: all([not y.lower() in x.lower() for y in stop_items]), item_description)

        item_description = "\n".join(item_description)

        image_url_list = response.xpath('//li[@class="vip-options-slideeach"]/a/@data-img').extract()

        # print(type(item_title))
        # print(type(item_description))

        if len(image_url_list) > 3:
            d = {
                'Item Title': item_title,
                'description': item_description,
                'Item Price': item_price,
                'Savings': item_savings,
                'Details': idetail
            }

            category_name = response.meta['dir_name']
            item_dir_url = os.path.join(self.base_dir, os.path.join(category_name, item_title))

            if not os.path.exists(item_dir_url):
                os.makedirs(item_dir_url)

            # save meta data

            with open(os.path.join(item_dir_url, 'metadata.txt'), 'w') as f:
                json.dump(d, f)

            # save images

            for i, img_url in enumerate(image_url_list):
                r = requests.get(img_url)
                with open(os.path.join(item_dir_url, 'image_{}.jpg'.format(i)), 'wb') as f:
                    f.write(r.content)

            # print(item_title)
            print('-->successfully saved\''+item_title + '\'data at :' + item_dir_url)

            yield d

        yield None









