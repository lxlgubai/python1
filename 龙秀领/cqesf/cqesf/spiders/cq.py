import scrapy

from cqesf.items import CqesfItem

class CqSpider(scrapy.Spider):
    name = "cq"
    allowed_domains = ["lianjia.com"]
    url = 'https://cq.lianjia.com/ershoufang/pg'
    set_page = 1
    start_urls = [url + str(set_page) + "/"]

    def parse(self, response):
        item = CqesfItem()
        divs = response.xpath('//ul[@class="sellListContent"]/li')
        for li in divs:
            item["title"] = li.xpath('./div[1]/div[1]/a/text()').extract()[0]  # 标题
            item["address"] = li.xpath('./div[1]/div[2]/div/a[1]/text()').extract()[0]  # 地址
            item["address_perimeter"] = li.xpath('./div[1]/div[2]/div/a[2]/text()').extract()[0]  # 地址周边
            item["Building_information"] = li.xpath('./div[1]/div[3]/div/text()').extract()[0]  # 楼房信息
            item["Price"] = li.xpath('./div[1]/div[6]/div[1]/span/text()').extract()[0]  # 总价
            item["data_price"] = li.xpath('./div[1]/div[6]/div[2]/span/text()').extract()[0]  # 平方单价
            yield item
            # time.sleep(2)
        self.set_page += 1
        next_url = self.url + str(self.set_page) + "/"
        yield scrapy.Request(next_url, callback=self.parse)
