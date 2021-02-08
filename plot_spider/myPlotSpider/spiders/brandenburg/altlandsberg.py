# -*- coding: utf-8 -*-

import scrapy
import hashlib
from scrapy.spiders import Spider

from myPlotSpider.factory.tool import Factories
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
            title = Factories.fix_field(plot_title_div.extract_first())
            # title = fix_field(plot_title_div.extract_first())
            plot_properties_div_list = plot.xpath("div[@class='item-properties']//text()").extract()
            # 这里得到的是一个包含描述分句的列表
            # 在这里对每一段文字进行预处理格式，以便后续存入数据库
            # 如果有图片的话，也可以进行相应处理...
            # todo
            bundesland = 'Brandenburg'  # 联邦州名
            county = 'Altlandsberg'  # 城市或地区名
            title = fix_field(plot_title_div.extract_first())
            plot_category_div = plot.xpath("div[@class='item-category']//text()")
            category = fix_field(plot_category_div.extract()[-1])
            properties = ''  # 在这里对之前提取的properties文本list对象进行处理
            # print("title: " + title + " ; category: " + category)
            # 提取image
            plot_properties_div = plot.xpath("div[@class='item-properties']")
            img_list = plot_properties_div.xpath("//img/@src")
            # 提取图片链接
            img_urls = []
            url = response.request.url  # 获取链接地址
            # 提取pdf链接
            # 将PDF文档定义为只有一个
            # pdf_url = ''
            plot_link_list = plot_properties_div.xpath("a/@href")
            # 一部分link是img，一部分link是pdf文档
            # todo

        """
        # title = response.xpath("//div[@class='item']").xpath("//div[@class='item-title']//text()").extract_first()
        # '<div class="item-title">Gutshof Gielsdorf<br></div>'
        # category = response.xpath("//div[@class='item']").xpath("//div[@class='item-category']//text()").extract_first()
        """
        # todo
        pass

    def parse_detail(self, response):
        # parse some detail information and pass to item object for further processing
        pass


def fix_field(field):
    return field.strip() if field else ''


def fix_properties_field(properties_field):
    return "".join(properties_field)  # convert html content to a string

