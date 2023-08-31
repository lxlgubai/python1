import scrapy

from qnzy1.items import Qnzy1Item

class QnSpider(scrapy.Spider):
    name = "qn"
    allowed_domains = ["qnzy.net"]
    url = 'https://www.qnzy.net/html/1090/'
    set_page = 1
    start_urls = [url]

    def parse(self, response):
        item =Qnzy1Item()
        div = response.xpath('//div[@class="label_adap_pic_com_ul26"]')
        for li in div:
            item["title"] = li.xpath('./div/div/div[2]/div/h3/a/text()').extract()[0]
            item["texts"] = li.xpath('./div/div/div[2]/div/p[1]/a/text()').extract()[0]
            item["Dates"] = li.xpath('./div/div/div[2]/div/p[2]/text()').extract()[0]
            yield item
        self.set_page += 1
        next_url = self.url + "list-"+str(self.set_page)+".html"
        yield scrapy.Request(next_url, callback=self.parse)
