# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item
from scrapy import Field


class MyplotspiderItem(scrapy.Item):
    """
        @scrapy.item，继承父类scrapy.Item的属性和方法，该类用于定义需要爬取数据的子段
    """
    # define the fields for your item here like:
    article_bundesland = scrapy.Field()  # 联邦州名
    article_county = scrapy.Field()  # 城市或地区名
    article_title = scrapy.Field()  # 标题
    article_content = scrapy.Field()  # 内容
    article_uid = scrapy.Field()  # 唯一识别id
    article_url = scrapy.Field()  # 链接地址
    article_img_urls = scrapy.Field()  # 图片链接地址 (图片链接为一个list)
    article_img_names = scrapy.Field()  # 图片名list ()


class ImagesrenameItem(scrapy.Item):
    # todo
    # image url, image name, image uid
    pass
