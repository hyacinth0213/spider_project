# -*- coding: utf-8 -*-

import scrapy
import hashlib
from scrapy.spiders import Spider

from myPlotSpider.factory.text_tool import Factories
from myPlotSpider.items import MyplotspiderItem


class AlttuchebandSpider(scrapy.Spider):
    name = 'breese_spider'
    allowed_domains = ['www.amt-badwilsnack-weisen.de/']
    start_urls = ['http://www.amt-badwilsnack-weisen.de/index.php?option=com_content&task=view&id=69&Itemid=125']

    bundesland_name = 'Brandenburg'
    county_name = 'Bad Wilsnack'

    def parse(self, response):
        content_div = response.xpath("//div[@id='content_area']/div[@class='contentpane']//text()")
        pass
