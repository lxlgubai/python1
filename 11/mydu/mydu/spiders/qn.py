import scrapy


class QnSpider(scrapy.Spider):
    name = "qn"
    allowed_domains = ["qnzy.net"]
    start_urls = ["http://qnzy.net/"]

    def parse(self, response):
        pass
