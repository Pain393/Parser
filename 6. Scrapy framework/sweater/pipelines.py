# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class SweaterPipeline:
    def open_spider(self, spider):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['sweater']

    def process_item(self, item, spider):
        collection_name = 'sweaters'
        self.db[collection_name].insert_one(item)

    def close_spider(self, spider):
        self.client.close()
