import scrapy

from lianjia.items import LianjiaItem

class LjSpider(scrapy.Spider):
    name = "lj"
    allowed_domains = ["cd.lianjia.com"]
    url = "https://cd.lianjia.com/zufang/pg2"
    set_page = 1
    start_urls = [url + str(set_page) + "/"]

    def parse(self, response):
        item = LianjiaItem()
        lis = response.xpath('//div[@class="content__list--item--main"]')

        for li in lis:
            item["url1"] = li.xpath('./p[1]/a/text()').extract()[0]
            item["url2"] = li.xpath('./p[2]/a[1]/text()').extract()[0]
            item["url3"] = li.xpath('./p[2]/text()').extract()[3]
            item["url4"] = li.xpath('./span/em/text()').extract()[0]
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page) + "/"
        yield scrapy.Request(next_url, callback=self.parse)
