import scrapy
from bs4 import BeautifulSoup
import re

class SinaNewsSpider(scrapy.Spider):
    name = 'sina_news'
    start_urls = [
        'https://news.sina.com.cn/'
    ]

    def parse(self,response):
        soup = BeautifulSoup(response.body,'html.parser')
        tags = soup.find_all('a',herf=re.compile(r"sina.*\d{4}-\d{2}-\d{2}.*shtml$"))
        for tag in tags:
            print(tag.text.strip())  