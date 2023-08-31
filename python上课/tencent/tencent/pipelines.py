# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import warnings

from itemadapter import ItemAdapter


class TencentPipeline:
    def process_item(self, item, spider):
        print("-" * 60)
        print(item["url1"])
        print(item["url2"])
        print(item["url3"])
        print(item["url4"])
        print(item["url5"])
        print("-" * 60)


class TencentPipeline_csv(object):
    def __init__(self):
        self.f = open("腾讯招聘.csv", "a", newline="")
        self.writer = csv.writer(self.f)
        self.writer.writerow(["标题", "地点", "公司", "技术支持", "工作经验"])

    def process_item(self, item, spider):
        L = [item["url1"], item["url2"], item["url3"], item["url4"], item["url5"]]
        self.writer.writerow(L)
        return item


import pymysql


class TencentPipeline_sql(object):
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="102030", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = "create database if not exists tencent character set utf8"
        u_db = "use tencent"
        c_tab = "create table if not exists tex(title varchar(200)," \
                "dediao varchar(255)," \
                "gongsi varchar(255)," \
                "jishu varchar(255)," \
                "gongzuo varchar(50))charset=utf8"
        warnings.filterwarnings("ignore")
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_tab)
        except Warning:
            pass
        ins = "insert into tex(title,dediao,gongsi,jishu,gongzuo) values(%s,%s,%s,%s,%s)"
        L = [item["url1"], item["url2"], item["url3"], item["url4"], item["url5"]]
        self.cursor.execute(ins, L)
        self.db.commit()
