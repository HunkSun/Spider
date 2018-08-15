# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from Jingdong.middlewares import browser


class JingdongPipeline(object):
    def process_item(self, item, spider):
        # print(item)
        return item


class MongoDBPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client['Jingdong']
        self.collection = self.db['lingshi']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
        browser.close()


class MySQLPipeline(object):
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          port=3306,
                                          db='spider',
                                          user='spider',
                                          password='sunhao446688',
                                          charset='utf8')
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        sql = 'insert into spider.jingdong(name, price, image, shop, commit) values(%s, %s, %s, %s, %s)'
        self.cursor.execute(sql, (item['name'], item['price'], item['image'], item['shop'], item['commit']))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.connection.close()
        browser.close()
