# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
from urllib.parse import quote
from baiduyun.items import *
from baiduyun.items import *

class DlspiderSpider(scrapy.Spider):
    name = 'dlSpider'
    allowed_domains = ['https://pan.baiduwp.com']
    start_urls = ['https://pan.baiduwp.com/s/?surl=1J-3mS42KKrCCSt-a4Lgr8Q&pwd=54wv']


    def parse(self, response):
        re = response
        js_function = 'javascript:void(0)'
        next_url = re.xpath(
            "//li[@class='list-group-item border-muted rounded text-muted py-2']/a/@href")
        next_path = re.xpath(
            "//li[@class='list-group-item border-muted rounded text-muted py-2']/a/text()")
        if len(next_url):
            #creating path 
            current_path = response.meta.get('path')
            if current_path:
                path = current_path+'/'+next_path
            else:
                path = next_path

            #decide to use selenium or not 
            if next_url == js_function:
                yield Request(response.url, callback=self.parse_dl, meta={'path': path}, flags=[1])
            else:
                yield Request(next_url, callback=self.parse, meta={'path':path})
        else:
            print('sth wrong')
  
    def parse_dl(self, response):
        try:
            link = response.xpath("//a[@class='dlink']/@href")
            path = response.meta.get('path')
            if link:
                target = Dl_address()
                target['path'] = path
                target['url'] = link
                yield target
        except Exception as e:
            print(e)


