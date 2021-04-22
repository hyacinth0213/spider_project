# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

import re
import os
import codecs
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


def process_item(item, spider):
    return item


class MyplotspiderPipeline(object):
    pass


class ImagesrenamePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # todo
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['img_urls']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            # 抓取文章标题作为图集名称
            yield Request(image_url, meta={'name': item['imgName']})
        pass


class PlotCsvPipeline(object):
    def __init__(self):
        self.file = codecs.open(filename='plot.csv', mode='w+', encoding='utf-8')
        print("***************************************************************")

    def process_item(self, item, spider):
        res = dict(item)
        # 将字典形式的值，转化成字符串写入文件
        json_str = json.dumps(res, ensure_ascii=False)
        self.file.write(json_str)
        self.file.write(',\n')

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
