import scrapy
from scrapy.spiders import Spider

from myPlotSpider.factory.text_tool import TextTools
from myPlotSpider.items import MyplotspiderItem


class BernaubeiberlinSpider(scrapy.Spider):
    name = 'bernaubeiberlin_spider'
    allow_domains = ['stab-bernau.de']
    start_urls = ['https://stab-bernau.de/wohnbaugrundstuecke/']

    bundesland_name = 'Brandenburg'
    county_name = 'Bernau bei Berlin'

    def parse(self, response, **kwargs):
        pass
