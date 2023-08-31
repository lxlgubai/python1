# import pymysql
# import warnings
#
# db=pymysql.connect(host="localhost",user="root",password="102030",charset="utf8")
#
# cursor=db.cursor()
#
# warnings.filterwarnings("ignore")
# try:
#     cursor.execute("create database if not exists spiderdb")
#     cursor.execute("use spiderdb")
#     cursor.execute("create table if not exists t1(id int)")
# except Warning:
#     pass
# ins="insert into t1 values(%s)"
# cursor.execute(ins,[23])
# # cursor.execute(ins,[99])
#
# db.commit()
# cursor.close()
# db.close()
#
# import requests
# headers={"User-Agent":"Mozilla/5.0"}
# url='https://gy.lianjia.com/ershoufang'
# html = requests.get(url=url,headers=headers)

import re
import csv

import requests


class lianjia:
    def __init__(self):
        self.headers={"User-Agent":"Mozilla/5.0"}
        self.baseurl='https://gy.lianjia.com/ershoufang'
    def readPage(self,url):
        # req=urllib.request.Request(url,headers=self.headers)
        req=requests.get(url,headers=self.headers)
        # res=urllib.request.urlopen(req)
        req.encoding="utf-8"
        # html=res.read().decode('utf-8')
        # print(html)
        html=req.text
        self.parsePage(html)
    def parsePage(self,html):
        p=re.compile('<div class="positionInfo">.*?<a href=".*?" target=".*?" data-log_index=".*?" data-el=".*?">(.*?)</a>'
                     '.*?<a href=".*?" target=".*?">(.*?)</a>'
                     '.*?<div class="totalPrice totalPrice2">.*?class=".*?">(.*?)</span><i>(.*?)</i>'
                     '.*?<div class="unitPrice" data-hid=".*?" data-rid=".*?" data-price=".*?"><span>(.*?)</span>',re.S)
        r_list=p.findall(html)
        # self.writePage(r_list)
        print (r_list)
    def writePage(self,r_list):
        with open("链家二手房.csv","a",newline='')as f:
            writer=csv.writer(f)
            writer.writerow(["地点","小区","总价","万","单价"])
        for n in r_list:
            with open("链家二手房.csv","a",newline="") as f:
                writer=csv.writer(f)
                A=[n[0],n[1],n[2],n[3],n[4]]
                writer.writerow(A)
                print("保存成功")
    def workOn(self):
        begin=int(input("请输入开始页："))
        end=int(input("请输入结束页："))
        for b in range(begin,end+1):
            if b==1:
                url=self.baseurl
                self.readPage(url)
            elif b==b:
                url=self.baseurl+"/pg"+str(b)+"/"
                self.readPage(url)
if __name__ == '__main__':
    zzc = lianjia()
    zzc.workOn()