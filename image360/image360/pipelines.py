# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class Image360Pipeline(object):
    def process_item(self, item, spider):
        return item


class MonggoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_cralwer(cls, crawler):
        return cls(
            mongo_uri=crawler.setting.get('MONGO_URI'),
            mongo_db=crawler.setting.get('MONGO_DB'),
        )

    def open_spider(self, spider):
        # self.client = pymongo.MongoClient(self.mongo_uri)   
        # self.db = self.client[self.mongo_db]
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        # self.db[item.collectionn].insert(dict(item))
        # return item
        self.db[item.collection].insert(dict(item))
        return item
    
    def close_spider(self, spider):
        self.client.close()


      
