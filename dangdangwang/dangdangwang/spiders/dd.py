import scrapy
from dangdangwang.items import DangdangwangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdangwang.com"]
    start_urls = ["http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-1"]

    def parse(self, response):
        result = DangdangwangItem()
        content = response.xpath('//*[@class="bang_list clearfix bang_list_mode"]/li')
        print(content)
        for li in content:
            # 1标题
            bt = li.xpath('./div[3]/a/text()').extract()[0]
            # 2现售价格
            sj = li.xpath('./div[@class="price"]/p/span/text()').extract()[0].replace('?', '')
            # 3定价
            dj = li.xpath('./div[@class="price"]/p/span/text()').extract()[1].replace('?', '')
            # 4折扣
            zk = li.xpath('./div[@class="price"]/p/span/text()').extract()[2].replace('折', '')
            # 5发行时间
            s_time = li.xpath('./div[@class="publisher_info"]/span/text()').extract_first().replace('/', '')
            # 6出版社
            press = li.xpath('./div[6]/a/text()').extract()[0] if len(
                li.xpath('./div[6]/a/text()').extract()) > 0 else '出版社不明'
            # 7评论人数
            plrs = li.xpath('./div[@class="star"]/a/text()').extract_first().replace('条评论', '')
            print(plrs)
            # 8推荐比列
            tj = li.xpath('./div[@class="star"]/span/text()').extract_first().replace('推荐', '')
            dzs = li.xpath('./div[@class="price"]/p[2]/text()').extract()[0].replace('：', '') if len(
                li.xpath('./div[@class="price"]/p[2]/text()').extract()) > 0 else '无电子书版本'
            result['bt'] = bt
            result['sj'] = sj
            result['dj'] = dj
            result['zk'] = zk
            result['s_time'] = s_time
            result['press'] = press
            result['plrs'] = plrs
            result['tj'] = tj
            result['dzs'] = dzs

            yield result
            for i in range(1, 26):
                url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-%d' % i
                yield Request(url, callback=self.parse)




