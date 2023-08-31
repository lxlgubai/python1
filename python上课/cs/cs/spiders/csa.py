import scrapy
from cs.items import CsItem

class CsaSpider(scrapy.Spider):
    name = "csa"
    allowed_domains = ["blog.csdn.net"]
    start_urls = ["https://blog.csdn.net/FRIGIDWINTER/article/details/129787961"]

    def parse(self, response):
        item = CsItem()
        item["url1"] = response.xpath('//h1[@id="articleContentId"]/text()').extract()[0]
        item["url2"] = response.xpath('//div[@class="bar-content"]/span[1]/text()').extract()[0]
        item["url3"] = response.xpath('//span[@class="read-count"]/text()').extract()[0]
        item["url4"] = response.xpath('//span[@class="get-collection"]/text()').extract()[0]
        yield item
