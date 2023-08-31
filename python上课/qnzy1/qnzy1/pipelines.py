# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import warnings

from itemadapter import ItemAdapter


class Qnzy1Pipeline:
    def process_item(self, item, spider):
        print("-" * 60)
        print(item["title"])
        print(item["texts"])
        print(item["Dates"])
        print("-" * 60)


class Qnzy1Pipeline_csv(object):
    def __init__(self):
        self.f = open("qnzy.csv", "a", newline="")
        self.writer = csv.writer(self.f)
        self.writer.writerow(["标题", "内容", "时间"])

    def process_item(self, item, spider):
        L = [item["title"], item["texts"], item["Dates"]]
        self.writer.writerow(L)
        return item


import pymysql


class Qnzy1Pipeline_sql(object):
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="102030", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = "create database if not exists qnzy character set utf8"
        u_db = "use qnzy"
        c_tab = "create table if not exists qn(title varchar(200)," \
                "texts varchar(255)," \
                "Dates varchar(50))charset=utf8"
        warnings.filterwarnings("ignore")
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_tab)
        except Warning:
            pass
        ins = "insert into qn(title,texts,Dates) values(%s,%s,%s)"
        L = [item["title"], item["texts"], item["Dates"]]
        self.cursor.execute(ins, L)
        self.db.commit()
