# -*- coding: utf-8 -*-
import scrapy


class Basic2Spider(scrapy.Spider):
    name = 'basic2'
    allowed_domains = ['https://www.sainsburys.co.uk']
    start_urls = ['http://https://www.sainsburys.co.uk/']

    def parse(self, response):
        pass
