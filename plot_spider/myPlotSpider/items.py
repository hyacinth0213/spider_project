# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyplotspiderItem(scrapy.Item):
    # define the fields for your item here like:
    bundesland = scrapy.Field()  # 联邦州名
    county = scrapy.Field()  # 城市或地区名
    title = scrapy.Field()  # 标题
    property = scrapy.Field()  # 内容
    uid = scrapy.Field()  # 唯一识别id
    url = scrapy.Field()  # 链接地址
    imgUrls = scrapy.Field()  # 图片链接地址（图片链接为一个list）
    imgNames = scrapy.Field()  # 图片名list
    # pass


class ImagesrenameItem(scrapy.Item):
    # todo
    # image url, image name, image uid
    pass
