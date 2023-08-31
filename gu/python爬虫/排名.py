# 导包
import re
import requests
import parsel
import csv

q = open('ss1.csv',mode='w',newline='')
csv_w = csv.DictWriter(q,fieldnames=['书名', '评分', '是否连载', '签约状态', '分类1', '分类2',
                                     '作者', '字数', '阅读数', '人气值', '更新张节', '更新时间',
                                     '总章数','详情页地址'])
csv_w.writeheader()
# url地址
url = 'https://www.qimao.com/paihang/boy/update/date/'

# headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 数据请求与获取
data_get = requests.get(url=url, headers=headers)
data_text = data_get.text
# print(data_text)

# 数据解析
html_url = re.findall('<div class="child-tabs-item menu-tab" data-v-3034b3ca><a href="(.*?)".*?>(.*?)</a></div>', data_text)
# print(html_url)
ppp = 'https://www.qimao.com'
for ac,b in html_url:
    #print(b)
    ss = ppp + ac
    bs = requests.get(url=ss,headers=headers)
    xx = bs.text

    dd= re.findall('<div class="txt-row" data-v-8696f7ca><a href="(.*?)" target="_blank" class="s-book-title" data-v-8696f7ca>(.*?)</a>.*?</div>',xx)
    for ll,dd in dd:
        ff = requests.get(url=ll,headers=headers)
        gg = ff.text
        # print(ll)
        skfs = parsel.Selector(gg)
        sddd = skfs.xpath('//div[@id="__nuxt"]/div/div/div[3]/div/div')
        for BookPage in sddd:
            # 书名
            BookTitle = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[1]/span[1]/text()').get()
            # 评分
            Grading = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[1]/span[2]/text()').get()

            # 是否连载
            SeriaLization = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[2]/em/text()').get()
            # 签约状态
            Sign = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[2]/em/em/text()').get()
            # 分类
            CateGory1 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[2]/em[3]/a/text()').get()
            CateGory2 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[2]/em[4]/a/text()').get()
            # 作者
            aaa5 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[3]/span[1]/em/a/text()').get()
            UserNaem = aaa5.strip(' \n ')
            # 字数
            Number = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[4]/span[1]/em/text()').get()
            # a = '万字'
            # a1 = '万次阅读'
            # a2 = '万累计人气值'
            # aaa61 = aaa6 + a
            aaa71 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[4]/span[2]/em/text()').get()

            aaa81 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[4]/span[3]/em/text()').get()

            aaa9 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[5]/span[2]/a/text()').get()
            aaa10 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[5]/span[3]/text()').get()

            aaa11 = BookPage.xpath('.//div[@class="book-detail-body"]/div/div[1]/ul/li[2]/div/span[2]/text()').get()
            aaa111 = aaa11.strip('章')
            kjh = {
                '书名': BookTitle,
                '评分': Grading,
                '是否连载': SeriaLization,
                '签约状态': Sign,
                '分类1': CateGory1,
                '分类2': CateGory2,
                '作者': UserNaem,
                '字数': Number,
                '阅读数': aaa71,
                '人气值': aaa81,
                '更新张节': aaa9,
                '更新时间': aaa10,
                '总章数': aaa111,
                '详情页地址': ll
            }
            csv_w.writerow(kjh)

