#爬取网页的内容
# -*- coding: utf-8 -*-
import scrapy

class W3schoolSpider(scrapy.Spider):
    name = 'w3school'
    allowed_domains = ['w3school.com.cn']
    start_urls = ['http://www.w3school.com.cn/cssref/css_selectors.asp',
                  'http://www.w3school.com.cn/xpath/']

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        pass