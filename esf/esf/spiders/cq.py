import scrapy
from esf.items import EsfItem


class CqSpider(scrapy.Spider):
    name = "cq"
    allowed_domains = ["cq.lianjia.com"]
    url = "https://cq.lianjia.com/ershoufang/"
    num = 1
    stary_urls = [url]

    def parse(self, response):
        item = EsfItem()
        divs = response.xpath('//ul[@class="sellListContent"]/li')
        for li in divs:
            rr = li.xpath('./div[1]/div[1]/a/text()').extract_first()
            print(li)
            # item['title'] = li.xpath('./div[1]/div[1]/a/text()').extract_first()
            # item['address'] = li.xpath('./div[1]/div[2]/div/a[1]/text()').extract_first()
        #     yield item
        # self.num += 1
        # next_url = self.url + 'pg' + str(self.num) + '/'
        # yield scrapy.Request(next_url,callback=self.parse)
