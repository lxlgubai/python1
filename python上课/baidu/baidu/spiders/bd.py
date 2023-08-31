import scrapy
from baidu.items import BaiduItem


class BdSpider(scrapy.Spider):
    name = "bd"
    allowed_domains = ["baidu.com"]
    start_urls = ["http://baidu.com/"]

    def parse(self, response):
        # 创建实例对象
        item = BaiduItem()
        item["url1"] = response.xpath('//div[@id="s-top-left"]/a[1]/text()').extract()[0]
        item["url2"] = response.xpath('//div[@id="s-top-left"]/a[2]/text()').extract()[0]
        item["url3"] = response.xpath('//div[@id="s-top-left"]/a[3]/text()').extract()[0]
        item["url4"] = response.xpath('//div[@id="s-top-left"]/a[4]/text()').extract()[0]
        item["url5"] = response.xpath('//div[@id="s-top-left"]/a[5]/text()').extract()[0]
        yield item # 生成器
