import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        # getall()方法和extract()方法一样，返回的都是符合要求的所有的数据，存在一个列表里
        # get() 、getall()方法是新的方法，extract() 、extract_first()方法是旧的方法。
        # extract() 、extract_first()方法取不到就返回None。
        # get() 、getall()方法取不到就raise一个错误。
        pass
