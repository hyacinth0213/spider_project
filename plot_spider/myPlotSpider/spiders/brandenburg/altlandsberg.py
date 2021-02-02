# -*- coding: utf-8 -*-

import scrapy
import hashlib
from scrapy.spiders import Spider

from myPlotSpider.items import MyplotspiderItem


class AltlandsbergSpider(scrapy.Spider):
    name = 'altlandsberg_spider'
    allowed_domains = ['www.altlandsberg.de']
    start_urls = ['https://www.altlandsberg.de/index.php?page=grundstuecke']

    def parse(self, response):
        plot_list = response.xpath("//div[@class='item']")
        # len = 3
        for plot in plot_list:
            item = MyplotspiderItem()
            plot_title_div = plot.xpath("div[@class='item-title']//text()")
            title = fix_field(plot_title_div.extract_first())
            plot_properties_div_list = plot.xpath("div[@class='item-properties']//text()").extract()
            # 这里得到的是一个包含描述分句的列表
            # 在这里对每一段文字进行预处理格式，以便后续存入数据库
            # 如果有图片的话，也可以进行相应处理...
            # todo
            bundesland = 'Brandenburg'  # 联邦州名
            county = 'Altlandsberg'  # 城市或地区名
            title = fix_field(plot_title_div.extract_first())
            category = ''
            properties = ''
            url = response.request.url  # 获取链接地址
            # todo

        """
        # title = response.xpath("//div[@class='item']").xpath("//div[@class='item-title']//text()").extract_first()
        # '<div class="item-title">Gutshof Gielsdorf<br></div>'
        # category = response.xpath("//div[@class='item']").xpath("//div[@class='item-category']//text()").extract_first()
        """
        # todo
        pass


def fix_field(field):
    return field.strip() if field else ''


def fix_properties_field(properties_field):
    return "".join(properties_field)  # convert html content to a string


def string_to_hash(s):  # 使用md5或uuid将字符串转换成唯一的数值
    m = hashlib.sha1(s.encode("utf-8")).hexdigest()
    return m
