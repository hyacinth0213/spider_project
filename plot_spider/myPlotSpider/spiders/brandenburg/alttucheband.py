# -*- coding: utf-8 -*-

import scrapy
import hashlib
from scrapy.spiders import Spider

from myPlotSpider.factory.tool import Factories
from myPlotSpider.items import MyplotspiderItem


class AlttuchebandSpider(scrapy.Spider):
    name = 'alttucheband_spider'
    allowed_domains = ['www.amt-golzow.de']
    start_urls = ['https://www.amt-golzow.de/immobilien/index/kategorie/cat/8/grundstueck']

    def parse(self, response, **kwargs):
        pass
