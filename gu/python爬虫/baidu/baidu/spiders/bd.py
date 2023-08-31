import scrapy


class BdSpider(scrapy.Spider):
    name = "bd"  # 程序名
    allowed_domains = ["baidu.com"]  # 域名
    start_urls = ["http://baidu.com/"]  # 数据获取首选访问URL地址

    def parse(self, response):
        with open('百度.html', 'a') as f:
            f.write(response.text)
