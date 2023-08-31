import scrapy


class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = ["http://csdn.net/"]

    def parse(self, response):
        with open('CSDN.html', 'a',encoding='gb18030') as f:
            f.write(response.text)
