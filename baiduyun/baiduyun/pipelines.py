# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.exceptions import DropItem


class ResourcePipline(object):
    def file_path(self, request, response=None, info=None):
        path = request.met.get('path')
        file_name = path.split('/')[-1]
        return file_name
    
    def item_completed(self, results, item, info):
        resource_paths = [x['path'] for ok, x in results if ok]
        if not resource_paths:
            raise DropItem('download failed')
        return item

    def get_media_requests(self, item, info):
        yield Request(item['url'])
