# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from Jingdong.items import JingdongItem
# from scrapy.xlib.pydispatch import dispatcher
# from scrapy import signals


class LingshiSpider(scrapy.Spider):
    name = 'lingshi'
    allowed_domains = ['jd.com']

    # start_urls = ['http://www.jd.com/']
    def start_requests(self):
        KEYWORD = quote('零食')
        for i in range(1, 5):
            url = 'https://search.jd.com/Search?keyword={keyword}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&stock=1' \
                  '&page={page}&s=1&click=0'.format(keyword=KEYWORD, page=str(2 * i - 1))
            req = scrapy.Request(url=url, callback=self.parse, meta={'use_selenium': True})
            print('正在爬取第{}页'.format(i))
            yield req

    def parse(self, response):
        products = response.xpath('//*[@id="J_goodsList"]/ul/li/div[@class="gl-i-wrap"]')
        print(len(products))
        for product in products:
            image = product.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
            price = product.xpath('.//div[@class="p-price"]//text()').extract()
            name = product.xpath('.//div[@class="p-name p-name-type-2"]/a/em//text()').extract()
            commit = product.xpath('.//div[@class="p-commit"]//text()').extract()
            shop = product.xpath('.//div[@class="p-shop"]//text()').extract()
            image = 'http:' + image
            price = ''.join(price).replace(r'\n', '').strip()
            name = ''.join(name).strip().replace(r'\n', '')
            commit = ''.join(commit).strip().replace(r'\n', '')
            shop = ''.join(shop).strip().replace(r'\n', '')
            # print(image)
            item = JingdongItem()
            item['name'] = name
            item['image'] = image
            item['price'] = price
            item['commit'] = commit
            item['shop'] = shop
            yield item
