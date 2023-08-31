import scrapy

from qxzy.items import QxzyItem


class ZySpider(scrapy.Spider):
    name = "zy"
    allowed_domains = ["qnzy.net"]
    start_urls = ["https://www.qnzy.net/html/1001/"]

    def parse(self, response):
        item = QxzyItem()
        lis = response.xpath('//ul[@class="adaplist103"]/li')
        for li in lis:
            item["url1"] = li.xpath('./a/text()').extract()[0]
            item["url2"] = li.xpath('./span/text()').extract()[0]
            yield item
