import scrapy
from bs4 import BeautifulSoup
import re
from sina.items import SinaItem

class SinaNewsSpider(scrapy.Spider):
    name = 'sina'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]
    custom_settings = {
        'LOG_LEVEL': 'ERROR'
    }
    

    def parse(self, response):
        for i in response.xpath('//div[@class=\'quote\']'):
            
            content = i.xpath('span[@class=\'text\']/text()').extract_first()
            author = i.xpath('span/small/text()').extract_first()
            tag = i.xpath('div[@class=\'tags\']//a/text()').extract()
            item = SinaItem(content = content, author = author, tag = tag)
            yield item
        # g to next page
        try:
            next_page = response.xpath('//li[@class=\'next\']/a/attribute::href').extract_first() 
            if next_page:
                next_page = response.urljoin(str(next_page))
                yield scrapy.Request(next_page, callback=self.parse)
        except Exception as identifier:
            print('error')

    



