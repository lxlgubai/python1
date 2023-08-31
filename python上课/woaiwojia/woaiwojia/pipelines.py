# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import warnings

from itemadapter import ItemAdapter


class WoaiwojiaPipeline:
    def process_item(self, item, spider):
        print("-" * 60)
        print(item["a"])
        print(item["b"])
        print(item["c"])
        print(item["d"])
        print(item["e"])
        print("-" * 60)


class WoaiwojiaPipeline_csv(object):
    def __init__(self):
        self.f = open("woaiwo.csv", "a", newline="")
        self.writer = csv.writer(self.f)
        self.writer.writerow(["标题", "类型", "地点", "小区", "价格"])

    def process_item(self, item, spider):
        L = [item["a"], item["b"], item["c"], item["d"], item["e"]]
        self.writer.writerow(L)
        return item


import pymysql


class WoaiwojiaPipeline_sql(object):
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="102030", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = "create database if not exists woaiwojia character set utf8"
        u_db = "use woaiwojia"
        c_tab = "create table if not exists wojia(a varchar(200)," \
                "b varchar(255)," \
                "c varchar(255)," \
                "d varchar(255)," \
                "e varchar(50))charset=utf8"
        warnings.filterwarnings("ignore")
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_tab)
        except Warning:
            pass
        ins = "insert into wojia(a,b,c,d,e) values(%s,%s,%s,%s,%s)"
        L = [item["a"], item["b"], item["c"], item["d"], item["e"]]
        self.cursor.execute(ins, L)
        self.db.commit()
