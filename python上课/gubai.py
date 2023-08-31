# 实训1
# import urllib.request
# reponte = urllib.request.urlopen("http://www.baidu.com")
# html = reponte.read().decode("utf-8")
# print(html)

# 实训2
# import urllib.request
# url = "http://www.baidu.com"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
# }
# request = urllib.request.Request(url,headers=headers)
# reponst = urllib.request.urlopen(request)
# html = reponst.read().decode("utf-8")
# print(html)

# 实训3
# import urllib.request
# url = "http://sve.dutpbook.com/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
# }
# request = urllib.request.Request(url=url,headers=headers)
# reponst1 = urllib.request.urlopen(request)
# html = reponst1.read().decode("utf-8")
# print(html)

# 实训4
# urllib.parse模块
# urlencode(字典编码) || quote(字符串编码) || &连接符
# 例：urllib.parse.urlencode("1":"2")
# import urllib.parse
# w = {"wd" : "黔南民族职业技术学院"}
# pode = urllib.parse.urlencode(w)
# print(pode)

# 实训5
# https://www.baidu.com/s?wd=美女；
# 实训1
# import urllib.request
# reponte = urllib.request.urlopen("http://www.baidu.com")
# html = reponte.read().decode("utf-8")
# print(html)

# 实训2
# import urllib.request
# url = "http://www.baidu.com"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
# }
# request = urllib.request.Request(url,headers=headers)
# reponst = urllib.request.urlopen(request)
# html = reponst.read().decode("utf-8")
# print(html)

# 实训3
# import urllib.request
# url = "http://sve.dutpbook.com/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
# }
# request = urllib.request.Request(url=url,headers=headers)
# reponst1 = urllib.request.urlopen(request)
# html = reponst1.read().decode("utf-8")
# print(html)

# 实训4
# urllib.parse模块
# urlencode(字典编码) || quote(字符串编码) || &连接符
# 例：urllib.parse.urlencode("1":"2")
# import urllib.parse
# w = {"wd" : "黔南民族职业技术学院"}
# pode = urllib.parse.urlencode(w)
# print(pode)

# 实训5
# https://www.baidu.com/s?wd=美女；
# import urllib.parse
# import urllib.request
# headers = {
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
# }
# baseurl = "https://www.baidu.com/s?"
# key = input("请输入你要搜索的内容：")
# d = {"wd": key}
# key1 = urllib.parse.urlencode(d)
# url = baseurl + key1
# request = urllib.request.Request(url, headers=headers)
# html = urllib.request.urlopen(request)
# html1 = html.read().decode("utf-8")
# ht = open("搜索.html", "w", encoding="utf-8")
# ht.write(html1)
# ht.close()
# print("保存成功")

# 实训6
# import urllib.parse
# import urllib.request
# headers = {
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
# }
# baseurl = "https://www.baidu.com/s?wd="
# key = input("请输入你要搜索的内容：")
# name = urllib.parse.quote(key)
# url = baseurl + name
# request = urllib.request.Request(url, headers=headers)
# html = urllib.request.urlopen(request)
# html1 = html.read().decode("utf-8")
# ht = open("搜索.html", "w", encoding="utf-8")
# ht.write(html1)
# ht.close()
# print("保存成功")


# 实训7
# import urllib.parse
# import urllib.request
# headers = {
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
# }
# baseurl = "https://www.baidu.com/s?wd="
# key = input("请输入你要搜索的内容：")
# name = urllib.parse.quote(key)
# url = baseurl + name
# request = urllib.request.Request(url, headers=headers)
# html = urllib.request.urlopen(request)
# html1 = html.read().decode("utf-8")
# ht = open("两会.html", "w", encoding="utf-8")
# ht.write(html1)
# ht.close()
# print("保存成功")

# 实训8
# https://tieba.baidu.com/f?kw= &pn=50

# import urllib.request
# import urllib.parse
# name1 = input("请输入要搜索的内容：")
# begin = int(input("请你输入搜索开始页："))
# end = int(input("请你输入搜索结束页："))
#
# kw = {"kw":name1}
# kw1 = urllib.parse.urlencode(kw)
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
# }
#
# for n in range(begin,end+1):
#     pn = (n-1)*50
#     basurl = "https://tieba.baidu.com/f?"
#     url = basurl+kw1+"&pn="+str(pn)
#     req = urllib.request.Request(url,headers=headers)
#     res = urllib.request.urlopen(req)
#     html = res.read().decode("utf-8")
#
#     filename= "第"+str(n)+"页.html"
#     with open(filename,"w",encoding="utf-8") as f:
#         print("正在获取第%d"%n)
#         f.write(html)
#         print("第%d获取成功"%n)
#         print("*"*25)


# 实训9  封装类
#
# import urllib.request
# import urllib.response
# import urllib.parse
# import time
#
#
# class BaiduS:
#     def __init__(self): # 初始化
#         self.headers = {
#                 "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
#             }
#         self.basurl = "https://tieba.baidu.com/f?"
#
#     def readPage(self,basurl):# 发送请求获取响应
#         req = urllib.request.Request(basurl, headers=self.headers)
#         res = urllib.request.urlopen(req)
#         time.sleep(2)
#         html = res.read().decode("utf-8")
#         return html
#
#     def wriePage(self,filename,html): # 数据保存到本地
#         with open(filename, "w", encoding="utf-8") as f:
#             f.write(html)
#             print("*"*30)
#
#     def wrokOn(self): # 主函数
#         name1 = input("请输入要搜索的内容：")
#         begin = int(input("请你输入搜索开始页："))
#         end = int(input("请你输入搜索结束页："))
#
#         kw = {"kw":name1}
#         kw1 = urllib.parse.urlencode(kw)
#         for n in range(begin, end+1):
#             pn = (n-1)*50
#             basurl = "https://tieba.baidu.com/f?"
#             url = basurl + kw1 + "&pn=" + str(pn)
#             html = self.readPage(url)
#             filename = "第" + str(n) + "页.html"
#             self.wriePage(filename,html)
#
#
# if __name__ == '__main__':
#     baidu = BaiduS()
#     baidu.wrokOn()


# 第二部分 ----------------------------------------

# 实训1

# import re
#
# html = """
# <div class="animal">
#      <p class="name">
#       <a title="Tiger"></a>
#       </p>
#       <p class="contents">
#       Two tiger two tigers run fast
#       </p>
# </div>
# <div class="animal">
#      <p class="name">
#       <a title="Rabbit"></a>
#       </p>
#       <p class="contents">
#       small white rabbit white and white
#       </p>
# </div>"""
# al=re.compile('<div class="animal">.*?<a title="(.*?)"></a>.*?<p class="contents">\n      (.*?)\n      </p>', re.S)
# r_list = al.findall(html)
# for text in r_list:
#     print("动物名称是", text[0])
#     print("动物描述是", text[1])

# 实训2
# import re
# import urllib.request

# class dalianSpider:
#     def __init__(self):
#         self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41"}
#         self.beasurl="https://blog.csdn.net/sunbaigui/article/details/129361991"
#     def readPage(self,url):
#         req=urllib.request.Request(url,headers=self.headers)
#         res=urllib.request.urlopen(req)
#         html=res.read().decode("utf-8")
#         self.passPage(html)
#         # print(html)
#     def passPage(self,html):
#         p=re.compile('<h1 class="title-article" id="articleContentId">(.*?)</h1>.*?<span class="time">于&nbsp;(.*?)&nbsp;发布</span>.*?<span class="read-count">(.*?)</span>',re.S)
#         r_list = p.findall(html)
#         # print(r_list)
#         for rt in r_list:
#             print("标题："+rt[0])
#             print("时间：" + rt[1])
#             print("浏览量：" + rt[2])
#
#     def wrokOn(self):
#         url=self.beasurl
#         self.readPage(url)
# if __name__=="__main__":
#     cs=dalianSpider()
#     cs.wrokOn()

# 实训3
# import re
# import urllib.request
#
# class Dlso:
#     def __init__(self):
#         self.headers={
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
#         }
#         self.baseurl='https://dutp.dlut.edu.cn/xwzx1/tzgg'
#
#     def read(self,url):
#         req = urllib.request.Request(url,headers=self.headers)
#         res = urllib.request.urlopen(req)
#         html = res.read().decode('utf-8')
#         self.pear(html)
#
#     def pear(self,html):
#         # print(html)
#         p = re.compile('<p>.*?<a href=".*?">(.*?)</a>.*?<em>(.*?)</em>.*?</p>',re.S)
#         r_t = p.findall(html)
#         # print(r_t)
#         for ir in r_t:
#             print("标题："+ir[0])
#             print("时间："+ir[1])
#
#     def word(self):
#         begin = int(input("开始"))
#         end = int(input("结束"))
#         for i in range(begin, end + 1):
#             if i == 1:
#                 url = self.baseurl + ".htm"
#                 self.read(url)
#             elif i == 2:
#                 url = self.baseurl + "/"+str(i)+".htm"
#                 self.read(url)
#
#             elif i == 3:
#                 url = self.baseurl + "/"+str(i-2)+".htm"
#                 self.read(url)
#
#
# if __name__ == '__main__':
#     dl = Dlso()
#     dl.word()

#
# import re
# import urllib.request
#
# class Dlso:
#     def __init__(self):
#         self.headers={
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
#         }
#         self.baseurl='http://192.168.88.89/s.php/zhaosheng/item-list-category-12814'
#
#     def read(self,url):
#         req = urllib.request.Request(url,headers=self.headers)
#         res = urllib.request.urlopen(req)
#         html = res.read().decode('utf-8')
#         self.pear(html)
#
#     def pear(self,html):
#         print(html)
#         p = re.compile('',re.S)
#         r_t = p.findall(html)
#         # print(r_t)
#         for ir in r_t:
#             print("标题："+ir[0])
#             print("时间："+ir[1])
#
#     def word(self):
#         begin = int(input("开始"))
#         end = int(input("结束"))
#         for i in range(begin, end + 1):
#             if i == 1:
#                 url = self.baseurl
#                 self.read(url)
#             elif i == 2:
#                 url = self.baseurl + "/"+str(i)+".htm"
#                 self.read(url)
#
#             elif i == 3:
#                 url = self.baseurl + "/"+str(i-2)+".htm"
#                 self.read(url)
#
#
# if __name__ == '__main__':
#     dl = Dlso()
#     dl.word()

# import urllib.request
# import re
# import csv
#
# class DBDY:
#     def __init__(self): #初始化
#         self.headers={"User-Agent":"Mozilla/5.0"}
#         self.baseurl="https://movie.douban.com/subject/34795100/comments?"
#     def readPage(self,url): #发送请求获取响应
#         req=urllib.request.Request(url,headers=self.headers)
#         res=urllib.request.urlopen(req)
#         html=res.read().decode("utf-8")
#         # print(html)
#         self.parsePage(html)
#     def parsePage(self,html): #爬取数据
#         zzc=re.compile('<div class="comment">.*?<span class="comment-info">.*?class="">(.*?)</a>.*?<span class="comment-time " title="(.*?)">.*?</span>.*?class="short">(.*?)</span>',re.S)
#         re_list=zzc.findall(html)
#         # print(re_list)
#         for gq in re_list:
#             print("用户名：",gq[0])
#             print("时间：",gq[1])
#             print("评论：",gq[2])
#             self.witePage(re_list)
#     def witePage(self,re_list): #数据保存
#         for gqzzc in re_list:
#             with open("DBDY.csv","a",newline="",encoding="utf-8") as z:
#                 writer=csv.writer(z)
#                 Z=[gqzzc[0],gqzzc[1],gqzzc[2]]
#                 writer.writerow(Z)
#     def workOn(self): #主函数
#         begin=int(input("输入开始页数："))
#         end=int(input("输入结束页数："))
#         for z in range(begin,end+1):
#             zz=(z - 1) * 20
#             url=self.baseurl+"start="+str(zz)
#             self.readPage(url)
#
# if __name__=="__main__":
#     zzc=DBDY()
#     zzc.workOn()

# import urllib.request
# import re
# import csv
# class lianjia:
#     def __init__(self):
#         self.headers={"User-Agent":"Mozilla/5.0"}
#         self.baseurl='https://gy.lianjia.com/ershoufang'
#     def readPage(self,url):
#         req=urllib.request.Request(url,headers=self.headers)
#         res=urllib.request.urlopen(req)
#         html=res.read().decode('utf-8')
#         # print(html)
#         self.parsePage(html)
#     def parsePage(self,html):
#         p=re.compile('<div class="positionInfo">.*?<a href=".*?" target=".*?" data-log_index=".*?" data-el=".*?">(.*?)</a>'
#                      '.*?<a href=".*?" target=".*?">(.*?)</a>'
#                      '.*?<div class="totalPrice totalPrice2">.*?class=".*?">(.*?)</span><i>(.*?)</i>'
#                      '.*?<div class="unitPrice" data-hid=".*?" data-rid=".*?" data-price=".*?"><span>(.*?)</span>',re.S)
#         r_list=p.findall(html)
#         self.writePage(r_list)
#         # print (r_list)
#         # for n in r_list:
#         #     print("地址：", n[0])
#         #     print("小区：", n[1])
#         #     print("总价：", n[2])
#         #     print("单位：", n[3])
#         #     print("单价：", n[4])
#     def writePage(self,r_list):
#         with open("链家二手房.csv","a",newline='')as f:
#             writer=csv.writer(f)
#             writer.writerow(["地点","小区","总价","万","单价"])
#         for n in r_list:
#             with open("链家二手房.csv","a",newline="") as f:
#                 writer=csv.writer(f)
#                 A=[n[0],n[1],n[2],n[3],n[4]]
#                 writer.writerow(A)
#                 print("保存成功")
#     def workOn(self):
#         begin=int(input("请输入开始页："))
#         end=int(input("请输入结束页："))
#         for b in range(begin,end+1):
#             if b==1:
#                 url=self.baseurl
#                 self.readPage(url)
#             elif b==b:
#                 url=self.baseurl+"/pg"+str(b)+"/"
#                 self.readPage(url)
# if __name__ == '__main__':
#     zzc = lianjia()
#     zzc.workOn()

# 1----------------
# import requests
#
# url = "http://www.baidu.com"
# headers={"User-Agent":"Mozilla/5.0"}
# res = requests.get(url=url,headers=headers)
# res.encoding="utf-8"
# html = res.text
# print(html)
# import requests
#
# url = 'https://sc.68design.net/photofiles/201503/wvFUgWWHXH.jpg'
# response = requests.get(url)
#
# with open('imagqe.jpg', 'wb') as f:
#     f.write(response.content)
# import warnings
#
# import requests
# import re
# import pymysql
#
# class Dlso:
#     def __init__(self):
#         self.headers={
#             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
#         }
#         self.baseurl='https://www.qnzy.net/zhaosheng/12814/'
#         self.db = pymysql.connect(host="localhost", user="root", password="102030", charset="utf8")
#         self.cursor = self.db.cursor()
#     def read(self,url):
#         req = requests.get(url=url,headers=self.headers)
#         req.encoding = 'utf-8'
#         html = req.text
#         self.pear(html)
#
#     def pear(self,html):
#         # print(html)
#         p = re.compile('<li class=.*?>.*?<span class=.*?>(.*?)</span>''.*?<a href=.*? target="_blank" title=(.*?)</a>',re.S)
#         r_t = p.findall(html)
#         self.write(r_t)
#
#     def write(self,r_t):
#         db_1="create database if not exists spiderdb1 character set utf8"
#         u_db="use spiderdb1"
#         c_tab = "create table if not exists qnzy(id int primary key auto_increment," \
#                 "housename varchar(255)," \
#                 "datetime varchar(50))charset=utf8"
#         warnings.filterwarnings("ignore")
#         try:
#             self.cursor.execute(db_1)
#             self.cursor.execute(u_db)
#             self.cursor.execute(c_tab)
#         except Warning:
#             pass
#         ins = "insert into qnzy(housename,datetime) values(%s,%s)"
#         for t in r_t:
#             housename=t[1]
#             village=t[0]
#             L=[housename,village]
#             self.cursor.execute(ins,L)
#             self.db.commit()
#
#     def word(self):
#         begin = int(input("开始页："))
#         end = int(input("结束页："))
#         for i in range(begin, end + 1):
#             if i == 1:
#                 url = self.baseurl
#                 self.read(url)
#             elif i == i:
#                 url = self.baseurl + "list-"+str(i)+".shtml"
#                 self.read(url)
#
#
#
# if __name__ == '__main__':
#     dl = Dlso()
#     dl.word()

# xpath解析

#
# html = '''<div class="wrapper">
#   <i class="iconfont icon-back" id="back"></i>
#   <a href="/" id="channel">新浪社会</a>
#   <ul id="nav">
#         <li><a href="http://domestic.firefox.sina.com/" title="国内">国内</a></li>
#         <li><a href="http://world.firefox.sina.com/" title="国际">国际</a></li>
#         <li><a href="http://mil.firefox.sina.com/" title="军事">军事</a></li>
#         <li><a href="http://photo.firefox.sina.com/" title="图片">图片</a></li>
#   </ul>
#   <i class="iconfont icon-liebiao" id="menu"></i>
# </div>'''
# from lxml import etree
#
# parsehtml = etree.HTML(html)
# htmls = parsehtml.xpath('//ul/li/a/@href')
# for hq in htmls:
#     print(hq)
# //a[@id="channel"]/text() //a标签标题
# //ul/li[1]/a/text()  // li下面第一个a标签标题
# //ul/li/a/text()  // li下面所有a标签标题
# //ul/li/a/@href   //获取a标签超链接

# import urllib.request
# import re
# import csv
#
# import requests
#
#
# class lianjia:
#     def __init__(self):
#         self.headers={"User-Agent":"Mozilla/5.0"}
#         self.baseurl='https://gy.lianjia.com/ershoufang'
#     def readPage(self,url):
#         # req=urllib.request.Request(url,headers=self.headers)
#         req=requests.get(url,headers=self.headers)
#         # res=urllib.request.urlopen(req)
#         req.encoding="utf-8"
#         # html=res.read().decode('utf-8')
#         # print(html)
#         html=req.text
#         self.parsePage(html)
#     def parsePage(self,html):
#         p=re.compile('<div class="positionInfo">.*?<a href=".*?" target=".*?" data-log_index=".*?" data-el=".*?">(.*?)</a>'
#                      '.*?<a href=".*?" target=".*?">(.*?)</a>'
#                      '.*?<div class="totalPrice totalPrice2">.*?class=".*?">(.*?)</span><i>(.*?)</i>'
#                      '.*?<div class="unitPrice" data-hid=".*?" data-rid=".*?" data-price=".*?"><span>(.*?)</span>',re.S)
#         r_list=p.findall(html)
#         self.writePage(r_list)
#         # print (r_list)
#     def writePage(self,r_list):
#         with open("链家二手房.csv","a",newline='')as f:
#             writer=csv.writer(f)
#             writer.writerow(["地点","小区","总价","万","单价"])
#         for n in r_list:
#             with open("链家二手房.csv","a",newline="") as f:
#                 writer=csv.writer(f)
#                 A=[n[0],n[1],n[2],n[3],n[4]]
#                 writer.writerow(A)
#                 print("保存成功")
#     def workOn(self):
#         begin=int(input("请输入开始页："))
#         end=int(input("请输入结束页："))
#         for b in range(begin,end+1):
#             if b==1:
#                 url=self.baseurl
#                 self.readPage(url)
#             elif b==b:
#                 url=self.baseurl+"/pg"+str(b)+"/"
#                 self.readPage(url)
# if __name__ == '__main__':
#     zzc = lianjia()
#     zzc.workOn()
#
# import re
# import warnings
#
# import pymysql
# import requests
#
#
# class lianjia:
#     def __init__(self):
#         self.headers={"User-Agent":"Mozilla/5.0"}
#         self.baseurl='https://gy.lianjia.com/ershoufang'
#         self.db = pymysql.connect(host="localhost", user="root", password="102030", charset="utf8")
#         self.cursor = self.db.cursor()
#
#     def readPage(self,url):
#         req=requests.get(url,headers=self.headers)
#         req.encoding="utf-8"
#         html=req.text
#         self.parsePage(html)
#     def parsePage(self,html):
#         p=re.compile('<div class="positionInfo">.*?<a href=".*?" target=".*?" data-log_index=".*?" data-el=".*?">(.*?)</a>'
#                      '.*?<a href=".*?" target=".*?">(.*?)</a>'
#                      '.*?<div class="totalPrice totalPrice2">.*?class=".*?">(.*?)</span><i>(.*?)</i>'
#                      '.*?<div class="unitPrice" data-hid=".*?" data-rid=".*?" data-price=".*?"><span>(.*?)</span>',re.S)
#         r_list=p.findall(html)
#         self.writePage(r_list)
#         # print (r_list)
#     def writePage(self,r_list):
#         db_1="create database if not exists spiderdb1 character set utf8"
#         u_db="use spiderdb1"
#         c_tab = "create table if not exists ljesf(id int primary key auto_increment," \
#                 "housename varchar(50)," \
#                 "village varchar(50)," \
#                 "unit_pri varchar(50)," \
#                 "unit_li varchar(50))charset=utf8"
#         warnings.filterwarnings("ignore")
#         try:
#             self.cursor.execute(db_1)
#             self.cursor.execute(u_db)
#             self.cursor.execute(c_tab)
#         except Warning:
#             pass
#         ins = "insert into ljesf(housename,village,unit_pri,unit_li) values(%s,%s,%s,%s)"
#         for t in r_list:
#             housename=t[0]
#             village=t[1]
#             unit_pr=t[2]
#             unit_li=t[4]
#             L=[housename,village,unit_pr,unit_li]
#             self.cursor.execute(ins,L)
#             self.db.commit()
#
#     def workOn(self):
#         begin=int(input("请输入开始页："))
#         end=int(input("请输入结束页："))
#         for b in range(begin,end+1):
#             if b==1:
#                 url=self.baseurl
#                 self.readPage(url)
#             elif b==b:
#                 url=self.baseurl+"/pg"+str(b)+"/"
#                 self.readPage(url)
# if __name__ == '__main__':
#     zzc = lianjia()
#     zzc.workOn()

# import requests
# from lxml import etree
#
#
# class Lianjia:
#     def __init__(self):
#         self.baseurl = "https://gy.lianjia.com/zufang/"
#         self.headers = {"User-Agent": "Mozilla/5.0"}
#
#     def getPage(self, url):
#         res = requests.get(url, headers=self.headers)
#         res.encoding = "utf-8"
#         html = res.text
#         # print(html)
#         self.parsePage(html)
#
#     def parsePage(self, html):
#         parsehtml = etree.HTML(html)
#         re_list = parsehtml.xpath('//div[@class="content__list"]/div/div/span/em/text()')
#         for a in re_list:
#             print(a)
#
#     def workOn(self):
#         url = self.baseurl
#         self.getPage(url)
#
#
# if __name__ == "__main__":
#     p = Lianjia()
#     p.workOn()

#
# import requests
# from lxml import etree
#
#
# class Baid:
#     def __init__(self):
#         self.baseurl = "https://gy.lianjia.com/zufang/"
#         self.headers = {"User-Agent": "Mozilla/5.0"}
#
#     def gat(self, url):
#         res = requests.get(url, headers=self.headers)
#         res.encoding = "utf-8"
#         html = res.text
#         self.parse(html)
#
#     def parse(self, html):
#         pars = etree.HTML(html)
#         r_list = pars.xpath('//div[@class="content__list--item--main"]/p[1]/a/text() | //div[@class="content__list--item--main"]/p[2]/a/text() | //div[@class="content__list--item--main"]/span/em/text() | //div[@class="content__list--item--main"]/span/text()')
#         for t in r_list:
#             print("1"+r_list[0].strip())
#
#     def work(self):
#         url = self.baseurl
#         self.gat(url)
#
#
# if __name__ == '__main__':
#     db = Baid()
#     db.work()
# # //div[@class="content__list"]/div/div/p[1]/a/text()
# # //div[@class="content__list"]/div/div/span/em/text()
# # //div[@class="content__list"]/div/div/p[2]/a/text()


# sellnium

# 查看版本：chrome://version/
# chromedriver下载地址：http://chromedriver.storage.googleapis.com/index.html
# 1.截图百度
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# driver.save_screenshot('百度首页.png')
# driver.quit()

# 2.
# import time
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# kw = driver.find_element_by_id("kw")
# kw.send_keys("帅哥")
# su = driver.find_element_by_id("su")
# su.click()
# time.sleep(5)
# driver.save_screenshot('帅哥.png')
# driver.quit()

# 3
# import time
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# name = input("请输入要搜索的内容")
# kw = driver.find_element_by_id("kw")
# kw.send_keys(name)
# su = driver.find_element_by_id("su")
# su.click()
# time.sleep(5)
# driver.save_screenshot('帅哥.png')
# driver.quit()


# 4
# import time

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# kw = driver.find_element_by_id("kw")
# name = input("请输入：")
# kw.send_keys(name)
# # 百度一下
# su=driver.find_element_by_id("su")
# su.click()
# time.sleep(8)
# driver.save_screenshot("搜索.png")
# driver.quit()

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.jd.com')
# kw = driver.find_element_by_id("key")
# name = input("请输入：")
# kw.send_keys(name)
# # 京东
# su=driver.find_element_by_class_name("button")
# su.click()
# time.sleep(8)
# driver.save_screenshot(name+".png")
# driver.quit()

# 6
# import time
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('https://cas.qnzy.net/lyuapServer/login')
#
# nam = driver.find_element_by_id('username')
# user = input("请输入学号")
# nam.send_keys(user)
#
# pas = driver.find_element_by_id('password')
# pasa = input("请输入密码")
# pas.send_keys(pasa)
#
# captcha = driver.find_element_by_id('captcha')
# capt = input("请输入验证码")
# captcha.send_keys(capt)
#
# bottom = driver.find_element_by_name('login')
# bottom.click()
# time.sleep(8)
# driver.save_screenshot('黔南职院.png')
# driver.quit()


# 9
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.huya.com/')
# kw = driver.find_element_by_id("key")
# name = input("请输入：")
# kw.send_keys(name)
# su=driver.find_element_by_class_name("button")
# su.click()
# time.sleep(8)
# driver.save_screenshot(name+".png")
# driver.quit()


# 10
# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.get("https://www.csdn.net/")
# time.sleep(3)
# browser.maximize_window()
# for i in range(3):#测试三次下拉
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)
# browser.close()

# 11
# from selenium import webdriver
# import time
# import csv
# i=1
# driver=webdriver.Chrome()
# driver.get("https://www.huya.com/l")
#
#
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(2)
#     r_list=driver.find_elements_by_xpath('//li[@class="game-live-item"]')
#     for r in r_list:
#         m=r.text.split('\n')
#         name=m[0]
#         type=m[1]
#         with open("虎牙.csv","a",newline="",encoding="gb18030") as f:
#             writer=csv.writer(f)
#             L=[name.strip(),type.strip()]
#             writer.writerow(L)
#
#     print("第%d页数据获取成功"%i)
#     i+=1
#     #实现翻页
#     if driver.page_source.find('laypge_last')!=-1:
#             name=driver.find_elements_by_class_name("laypage_next")
#             name.click()
#     else:
#             print("数据获取结束！！！")

#
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# import csv
#
# driver.get("https://www.douyu.com/directory/all")
# i = 1
# while True:
#     driver.execute_script(
#         "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)
#     r_list = driver.find_elements_by_xpath('//li[@class="layout-Cover-item"]')
#
#     for r in r_list:
#         m = r.text.split('\n')
#
#         if m == ['']:
#             pass
#         else:
#             name = m[0]
#             type = m[1]
#         # L=[name,type]
#         # print(m)
#             with open("斗鱼.csv", "a", newline="", encoding="gb18030") as f:
#                 writer = csv.writer(f)
#                 L = [name.strip(), type.strip()]
#                 writer.writerow(L)
#     print("第%d页数据获取成功" % i)
#     i += 1
#     if driver.page_source.find('dy-Pagination-item') != -1:
#         name = driver.find_element_by_class_name("dy-Pagination-item-custom")
#         name.click()
#     else:
#         print("数据获取结束!!!")
# import csv
#
# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.jd.com/")
# k1 = driver.find_element_by_id("key")
# name = input("请输入关键字")
# k1.send_keys(name)
# su = driver.find_element_by_class_name("button")
# su.click()
# i = 1
# while True:
#     driver.execute_script(
#         "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)
#     r_list = driver.find_elements_by_xpath('//li[@class="gl-item"]')
#     for r in r_list:
#         m = r.text.split('\n')
#         yy = m[0]
#         title = m[1]
#         pl = m[3]
#         name = m[4]
#         # L=[yy.strip(), title.strip(),pl.strip(),name.strip()]
#         # print(L)
#         with open("京东.csv", "a", newline="", encoding="gb18030") as f:
#             writer = csv.writer(f)
#             L = [yy.strip(), title.strip(), pl.strip(), name.strip()]
#             writer.writerow(L)
#         print("第%d页数据获取成功" % i)
#     i += 1


# -------------------------------------------------------0


# -------------------------------------------------------1


# -------------------------------------------------------0

# scrapy Engine(引擎) 总指挥：负责数据和信号在不同模型间的传递
# Scheduler(调试器)
# Downloader(下载器)
# spider(爬虫)
# Item Pipeline(管道)
# Downloader Middlewares(下载中间建)

# 创建项目 scrapy startproject baidu
# 进入项目 cd baidu
# scrapy genspider bd baidu.com

# 运行 scrapy crawl bd

# 1,先编写items.py
# 2,修改爬虫文件
# 3修改pipelines.py
# 4修改settings.py
# 运行 scrapy crawl bd
# -------------------------------------------------------1

# -------------------------------0

# -------------------------------1


# ----------------------------------------------------0
# scrapy crawl qn -o qn.csv  保存csv
# ------------------------------------------------------1

# import pyautogui
#
# # 获取当前屏幕的大小
# screen_width, screen_height = pyautogui.size()
#
# # 从左上角开始截取整个屏幕的图像
# screenshot = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))
#
# # 保存截图到文件
# screenshot.save('screenshot.png')

#
# import tkinter as tk
# import pyautogui
# from PIL import ImageGrab
#
# # 创建主窗口对象
# root = tk.Tk()
#
# # 设置窗口标题和大小
# root.title("透视")
# root.geometry("600x500")
#
# # 将背景设置为透明
# # root.attributes('-alpha', 0.2)
#
# # 创建标签
# label = tk.Label(root, height=600, width=500)
# label.pack()
#
#
# def update_screen():
#     screen_width, screen_height = pyautogui.size()
#     screenshot = pyautogui.screenshot(region=(0, 0, screen_width, screen_height))
#     label.img = screenshot  # 保持引用，避免被垃圾回收
#
#     root.after(100, update_screen)  # 每100毫秒更新一次屏幕截图
#
# update_screen()
#
#
# # 进入主事件循环
# root.mainloop()
# import response

import requests
import json

url = 'https://push2.eastmoney.com/api/qt/clist/get?cb=jQuery112304159084124714212_1687769898410&fid=f62&po=1&pz=50&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A0%2Bt%3A6%2Bf%3A!2%2Cm%3A0%2Bt%3A13%2Bf%3A!2%2Cm%3A0%2Bt%3A80%2Bf%3A!2%2Cm%3A1%2Bt%3A2%2Bf%3A!2%2Cm%3A1%2Bt%3A23%2Bf%3A!2%2Cm%3A0%2Bt%3A7%2Bf%3A!2%2Cm%3A1%2Bt%3A3%2Bf%3A!2&fields=f12%2Cf14%2Cf2%2Cf3%2Cf62%2Cf184%2Cf66%2Cf69%2Cf72%2Cf75%2Cf78%2Cf81%2Cf84%2Cf87%2Cf204%2Cf205%2Cf124%2Cf1%2Cf13'

response = requests.get(url)
if response.status_code == 200:
    data = response.text
    start_index = data.find('(') + 1
    end_index = data.rfind(')')
    json_data = data[start_index:end_index]
    response_data = json.loads(json_data)
    diff_data = response_data['data']['diff']
    for i in diff_data:
        f1_value = i['f14']
        f2_value = i['f66']
        print(f1_value)
        print(f2_value)
else:
    print("失败")

