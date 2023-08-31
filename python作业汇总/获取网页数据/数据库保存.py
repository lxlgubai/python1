# 导包
import re
import requests
import parsel
from pymysql import connect


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

            aaa71 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[4]/span[2]/em/text()').get()

            aaa81 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[4]/span[3]/em/text()').get()

            aaa9 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[5]/span[2]/a/text()').get()
            aaa10 = BookPage.xpath('.//div[@class="book-detail-header"]/div/div[1]/div[2]/div[5]/span[3]/text()').get()

            aaa11 = BookPage.xpath('.//div[@class="book-detail-body"]/div/div[1]/ul/li[2]/div/span[2]/text()').get()
            aaa111 = aaa11.strip('章')


            jkh1 = []
            jkh1.append([BookTitle,Grading,SeriaLization,CateGory1,aaa71,aaa81])
            print(jkh1)
            # conn = connect(host='localhost', port=3306, database='name2', user='root', password='102030',
            #                charset='utf8')
            # csl = conn.cursor()
            # n = 1
            # for jkh in jkh1:
            #     try:
            #         csl.execute('INSERT INTO fiction1(`name`,`moods`,`classify`,`serialize`,`score`,`read`) VALUES(%s,%s,%s,%s,%s,%s);', (jkh[0], jkh[1], jkh[2], jkh[3], jkh[4], jkh[5]))
            #
            #         conn.commit()
            #     except Exception as e:
            #         conn.rollback()# 游标
            #         print('第'+ str(n)+'错误')
            #         n +=1
            #
            # conn.close()
            # csl.close()
            # print('完成')

