import scrapy
from lianjia.items import LianjiaItem

class LjSpider(scrapy.Spider):
    name = "lj"
    allowed_domains = ["gy.lianjia.com"]
    url = 'https://gy.lianjia.com/zufang/pg'
    set_page = 1
    start_urls = [url+str(set_page)+"/#contentList"]

    def parse(self, response):
        item = LianjiaItem()
        div = response.xpath('//div[@class="content__list--item--main"]')
        for li in div:
            item["title"] = li.xpath('./p[1]/a[1]/text()').extract()[0]
            item["address"] = li.xpath('./p[2]/a[1]/text()').extract()[0]
            item["money"] = li.xpath('./span/em/text()').extract()[0]
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page)
        yield scrapy.Request(next_url, callback=self.parse)
        # item["title"] = response.xpath('//a [@class="twoline"]/text()').extract()[0]

