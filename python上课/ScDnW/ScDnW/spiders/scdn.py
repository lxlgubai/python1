import scrapy
from ScDnW.items import ScdnwItem

class ScdnSpider(scrapy.Spider):
    name = "scdn"
    allowed_domains = ["csdn.net"]
    start_urls = ["https://blog.csdn.net/FRIGIDWINTER/article/details/129787961"]

    def parse(self, response):
        item = ScdnwItem()
        item["url1"] = response.xpath('//div[@class="article-title-box"]/h1/text()').extract()[0]
        item["url2"] = response.xpath('//div[@class="bar-content"]/span[1]/text()').extract()[0]
        item["url3"] = response.xpath('//div[@class="bar-content"]/span[2]/text()').extract()[0]
        item["url4"] = response.xpath('//div[@class="bar-content"]/a[2]/span[2]/text()').extract()[0]