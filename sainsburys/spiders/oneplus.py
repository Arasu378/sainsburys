# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy import Request
os.environ["https_proxy"] = "http://19.12.48.64:83"
os.environ["http_proxy"] = "http://19.12.48.64:83"
from sainsburys.oneplus_items import OnePlusItem

class OneplusSpider(scrapy.Spider):
    name = 'oneplus'
    allowed_domains = ['gsmarena.com']
    # https://www.gsmarena.com/oneplus-phones-95.php
    # https://www.gsmarena.com/samsung-phones-9.php
    start_urls = ['https://www.gsmarena.com/oneplus-phones-95.php']

    def parse(self, response):
        item = OnePlusItem()
        urls = response.xpath('//div[@class="makers"]/ul/li')
        mobiles = response.xpath('//div[@class="brandmenu-v2 light l-box clearfix"]/ul/li')
        l = -1
        for mobile in mobiles:
            l = l + 1
            print('Total Mobile Url')
            print(response.urljoin(mobile.css('a::attr(href)').extract_first().strip()))
            print((mobile.css('a::text').extract_first().strip()))
        # urls = response.xpath('//div[@class="makers"]/ul/li/a/img/@src').extract()
        i = -1
        print('Request URL :: ')
        print(response.request.url) 
        for url in urls:
            i = i + 1
            reference_url = response.urljoin(url.css('a::attr(href)').extract_first().strip())
            item['referenceLink'] = reference_url
            # item['referenceLink'] = response.urljoin(url.xpath('//a/@href').extract_first().strip())
            item['image'] = url.xpath('//a/img/@src').extract()[i].strip()
            item['description'] = url.xpath('//a/img/@title').extract()[i].strip()
            item['deviceName'] = url.xpath('//a/strong/span/text()').extract()[i].strip()           
           
            yield response.follow(reference_url, callback=self.mobile_description)
           
            yield item

        try:
             next_page = response.xpath('//a[@class="pages-next"]/@href').extract()[0].strip()
             if next_page:
                i = -1
                print('pageNo: ')
                next_url = response.urljoin(next_page)
                print(next_url)
                # yield Request(next_url, callback=self.parse)
                yield response.follow(next_url, callback=self.parse)
             else:
                print("no Pages")
        except:
            print('Exception')
       
        pass

    def mobile_description(self, response):
        print('Detail Page URL: : ')
        print(response.request.url)

        spec_list = response.xpath('//div[@id="specs-list"]')
        i = -1
        print('Table Data : :')
        print(response.xpath('//div[@id="specs-list"]').extract()[0])
        for table in spec_list:
            i = i + 1
            try:
                data = table.xpath('//table/tbody/tr[@class="tr-hover"]/th/text()').extract()[i].strip()
                print('TABLE')
                print(data)
            except Exception as e:
                print('Exception Details')
                print(e)
            
        pass
   
        
