import scrapy
from scrapy.spiders import Spider


class AltlandsbergSpider(scrapy.Spider):
    name = 'altlandsberg_spider'
    allowed_domains = ['www.altlandsberg.de']
    start_urls = ['https://www.altlandsberg.de/index.php?page=grundstuecke']

    def parse(self, response):
        plot_list = response.xpath("//div[@class='item']").extract()
        # len = 3
        for i in range(0, len(plot_list)):
            print(i)
            # todo
            pass
        title = response.xpath("//div[@class='item']").xpath("//div[@class='item-title']//text()").extract_first()
        # '<div class="item-title">Gutshof Gielsdorf<br></div>'
        category = response.xpath("//div[@class='item']").xpath("//div[@class='item-category']//text()").extract_first()
        pass
