# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
from items import Image360Item


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['images.so.com']
    start_urls = ['http://images.so.com/']

    def start_requests(self):
        data = {}
        base_url = 'https://image.so.com/zjl?'
        for p in range(1, 4):
            data['sn'] = p*30
            params = urlencode(data)
            url = base_url + params
            yield Request(url, self.parse)

    def parse(self, response):
        results = json.loads(response.text)
        for image in results['list']:
            item = Image360Item()
            item['id'] = image['image']
            item['url'] = image['url']
            item['title'] = image['title']
            yield item
            
