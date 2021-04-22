# -*- coding: utf-8 -*-

import scrapy
import hashlib
from scrapy.spiders import Spider

from myPlotSpider.factory.text_tool import Factories
from myPlotSpider.items import MyplotspiderItem


class AlttuchebandSpider(scrapy.Spider):
    name = 'alttucheband_spider'
    allowed_domains = ['www.amt-golzow.de']
    start_urls = ['https://www.amt-golzow.de/immobilien/index/kategorie/cat/8/grundstueck']

    bundesland_name = 'Brandenburg'
    county_name = 'Alt Tucheband'

    def parse(self, response):
        pass
