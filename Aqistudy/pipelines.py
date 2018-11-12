# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import pymongo
import redis
from scrapy.exporters import CsvItemExporter


# 数据源的管道
class AqistudyDataPipeline(object):
    def process_item(self, item, spider):
        item['crawl_time'] = datetime.utcnow()
        item['spider'] = spider.name
        return item

# csv文件
class AqistudyCsvPipeline(object):

    def open_spider(self, spider):
        self.file = open('aqistudy.csv', 'wb')
        self.writer = CsvItemExporter(self.file)
        self.writer.start_exporting()

    def process_item(self, item, spider):
        self.writer.export_item(item)
        return item

    def close_spider(self, spider):
        self.writer.finish_exporting()
        self.file.close()

# redis管道
class AqistudyRedisPipeline(object):
    def open_spider(self, spider):
        self._redis = redis.StrictRedis(host='127.0.0.1', port=6379)
        self._aqistudykey = 'aqistudy_key'

    def process_item(self, item, spider):
        self._redis.lpush(self._aqistudykey, dict(item))
        return item

# mongodb管道
class AqistudyMongodbPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=6379)
        self.collection = self.client.Aqistudy.aqistady

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()