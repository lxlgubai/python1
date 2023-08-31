import json

import scrapy
from tencent.items import TencentItem


class TexSpider(scrapy.Spider):
    name = "tex"
    allowed_domains = ["careers.tencent.com"]
    # https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex=1&pageSize=10
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex='
    set_page = 1
    start_urls = [url + str(set_page) + "&pageSize=10"]

    def parse(self, response):
        item = TencentItem()

        content = json.loads(response.body.decode())
        jobs = content['Data']['Posts']
        # print(jobs)
        for data in jobs:
            item['url1'] = data['RecruitPostName']
            item['url2'] = data['LocationName']
            item['url3'] = data['BGName']
            item['url4'] = data['CategoryName']
            item['url5'] = data['RequireWorkYearsName']
            yield item
        self.set_page += 1
        next_url = self.url + str(self.set_page) + "&pageSize=10"
        yield scrapy.Request(next_url, callback=self.parse)
