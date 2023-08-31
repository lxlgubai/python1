import scrapy
from woaiwojia.items import WoaiwojiaItem

class WojiaSpider(scrapy.Spider):
    name = "wojia"
    allowed_domains = ["5i5j.com"]
    url = "https://bj.5i5j.com/zufang/w3"
    set_page = 1
    start_urls = [url]

    def parse(self, response):
        item = WoaiwojiaItem()

        div = response.xpath('//ul[@class="pList rentList"]/li/div[2]')
        for li in div:
            item["a"] = li.xpath('./h3/a/text()').extract()[0]
            item["b"] = li.xpath('./div[1]/p[1]/text()').extract()[0]
            item["c"] = li.xpath('./div[1]/p[2]/text()').extract()[0]
            item["d"] = li.xpath('./div[1]/p[2]/a/text()').extract()[0]
            item["e"] = li.xpath('./div[1]/div/p/strong/text()').extract()[0]
            yield item
        self.set_page += 1
        next_url = self.url + "n"+str(self.set_page)+"/"
        yield scrapy.Request(next_url, callback=self.parse)

