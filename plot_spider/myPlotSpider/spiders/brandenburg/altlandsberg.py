# -*- coding: utf-8 -*-

import scrapy
import hashlib
from scrapy.spiders import Spider

from myPlotSpider.factory.text_tool import TextTools
from myPlotSpider.items import MyplotspiderItem


class AltlandsbergSpider(scrapy.Spider):
    name = 'altlandsberg_spider'
    allowed_domains = ['www.altlandsberg.de']
    start_urls = ['https://www.altlandsberg.de/index.php?page=grundstuecke']

    def parse(self, response):
        """
            @params:response,提取response中特定字段信息
        """
        plot_list = response.xpath("//div[@class='item']")
        # len = 3
        # index = 0
        for plot in plot_list:
            index = index + 1
            item = MyplotspiderItem()
            plot_title_div = plot.xpath("div[@class='item-title']//text()")
            title = TextTools.fix_field(plot_title_div.extract_first())
            title = fix_field(plot_title_div.extract_first())
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
            properties = plot_properties_div_list  # 将描述的string列表直接传给properties变量
            # 对properties内容进行处理
            # TODO...
            # 提取image
            # plot_properties_div = plot.xpath("div[@class='item-properties']")
            # 提取图片链接list
            # img_urls = plot_properties_div.xpath("a/img/@src").extract()
            url = response.request.url  # 获取链接地址
            # 提取pdf链接
            # plot_link_list = plot_properties_div.xpath("a/@href")
            # 一部分link是img, 一部分link是pdf文档, 对其进行分类
            # TODO...
            item['article_bundesland'] = bundesland
            item['article_county'] = county
            # item['article_title'] = title
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
