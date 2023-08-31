import scrapy

from bgesf.items import BgesfItem


class BkSpider(scrapy.Spider):
    name = "bk"
    allowed_domains = ["cd.ke.com"]
    url = "https://cd.ke.com/ershoufang/pg"
    set_page = 1
    start_urls = [url + str(set_page) + "/"]

    def parse(self, response):
        item = BgesfItem()
        lis = response.xpath('//li[@class="clear"]')

        for li in lis:
            item["url1"] = li.xpath('./div/div[1]/a/text()').extract()[0]
            item["url2"] = li.xpath('./div/div[2]/div[1]/div/a/text()').extract()[0]
            item["url3"] = li.xpath('./div/div[2]/div[5]/div[1]/span/text()').extract()[0]
            item["url4"] = li.xpath('./div/div[2]/div[5]/div[2]/span/text()').extract()[0]
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page) + "/"
        yield scrapy.Request(next_url, callback=self.parse)
