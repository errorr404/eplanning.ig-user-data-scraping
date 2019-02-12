# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class EplanningSpider(scrapy.Spider):
    name = 'eplanning'
    allowed_domains = ['eplanning.ie']
    start_urls = ['http://eplanning.ie/']

    def parse(self, response):
        urls = response.xpath('//a/@href').extract()
        for url in urls:
            if '#' == url:
                pass
            else:
                yield Request(url,callback=self.parse_application)

    def parse_application(self,response):
        pass
