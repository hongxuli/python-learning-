# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo

class SinaPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['content']:
            if len(item['content']) > self.limit:
                item['content'] = item['content'][0:self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('missing text')


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        #name = item.__class__.name
        name = 'quotes'
        self.db[name].insert(dict(item))
        return item

    def close_spider(self,spider):
        self.client.close()