import scrapy
from scrapy.spiders import Spider

from myPlotSpider.items import MyplotspiderItem


class AltlandsbergSpider(scrapy.Spider):
    name = 'altlandsberg_spider'
    allowed_domains = ['www.altlandsberg.de']
    start_urls = ['https://www.altlandsberg.de/index.php?page=grundstuecke']

    def parse(self, response):
        plot_list = response.xpath("//div[@class='item']")
        # len = 3
        for i in range(0, len(plot_list)):
            item = MyplotspiderItem()

            plot_div = plot_list[i]
            bundesland = 'Brandenburg'
            county = 'Altlandsberg'
            title = ''
            category = ''
            properties = ''
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


def fix_html_field(html_field):
    return "".join(html_field)  # convert html content to a string

