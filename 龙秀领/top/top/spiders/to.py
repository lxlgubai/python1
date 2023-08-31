import time

import requests
import scrapy
from lxml import etree

from top.items import TopItem


class ToSpider(scrapy.Spider):
    name = "to"
    allowed_domains = ["top.chinaz.com"]
    url = "https://top.chinaz.com/hangye/index"
    set_page = 1
    start_urls = [url + '.html']

    def parse(self, response):
        item = TopItem()
        ur = response.xpath('//ul[@class="listCentent"]/li/div[1]')
        u = "https://top.chinaz.com"
        for urs in ur:
            ht = urs.xpath('./a/@href').extract()[0]
            # print("*" * 60)
            url2 = u + ht
            html = requests.get(url2)
            html1 = html.text
            tit = etree.HTML(html1)
            DD = tit.xpath('//*[@id="content"]/div[4]/div/div[2]')
            for dd in DD:
                item['title'] = dd.xpath('./div[1]/div/h2/text()')[0]  # 标题
                item['rank'] = dd.xpath('./div[2]/ul/li[1]/p[1]/a/text()')[0].replace(' ', '')  # 排名
                try:
                    baidu_flow = dd.xpath('./div[6]/table/tbody[1]/tr/td[1]/comdiv[1]/text()')[0].replace('万', '')
                    baidu_index = dd.xpath('./div[6]/table/tbody[1]/tr/td[2]/comdiv/text()')[0].replace('万', '')
                    month_index = dd.xpath('./div[6]/table/tbody[1]/tr/td[3]/comdiv/text()')[0].replace('万', '')
                    google_index = dd.xpath('./div[6]/table/tbody[2]/tr/td[1]/comdiv/text()')[0].replace('万', '')
                    baidu_backlink = dd.xpath('./div[6]/table/tbody[1]/tr/td[5]/comdiv[1]/text()')[0].replace('万', '')
                    google_backlink = dd.xpath('./div[6]/table/tbody[2]/tr/td[2]/comdiv/text()')[0].replace('万', '')
                    qihoo_index = dd.xpath('./div[6]/table/tbody[2]/tr/td[3]/comdiv/text()')[0].replace('万', '')
                    qihoo_backlink = dd.xpath('./div[6]/table/tbody[2]/tr/td[4]/comdiv/text()')[0].replace('万', '')
                    sogou_index = dd.xpath('./div[6]/table/tbody[2]/tr/td[5]/comdiv/text()')[0].replace('万', '')
                    backlink = dd.xpath('./div[6]/table/tbody[2]/tr/td[6]/comdiv/text()')[0].replace('万', '')
                except IndexError:
                    baidu_flow = 0
                    baidu_index = 0
                    month_index = 0
                    google_index = 0
                    baidu_backlink = 0
                    google_backlink = 0
                    qihoo_index = 0
                    qihoo_backlink = 0
                    sogou_index = 0
                    backlink = 0
                item['baidu_flow'] = baidu_flow  # 百度预估流量
                item['baidu_index'] = baidu_index  # 百度收录
                item['month_index'] = month_index  # 单月收录
                item['google_index'] = google_index  # 谷歌收录
                item['baidu_backlink'] = baidu_backlink  # 百度反链数
                item['google_backlink'] = google_backlink  # 谷歌反链数
                item['qihoo_index'] = qihoo_index  # 360收录
                item['qihoo_backlink'] = qihoo_backlink  # 360反链数
                item['sogou_index'] = sogou_index  # 搜狗收录
                item['backlink'] = backlink  # 反链数
                yield item
                # time.sleep(1)
        self.set_page += 1
        next_url = self.url + "_" + str(self.set_page) + ".html"
        yield scrapy.Request(next_url, callback=self.parse)
