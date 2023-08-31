# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import warnings

import pymysql
from itemadapter import ItemAdapter


class TopPipeline:
    def process_item(self, item, spider):
        print("-" * 60)
        print(item["title"])
        print(item["rank"])
        print(item["baidu_flow"])
        print(item["baidu_index"])
        print(item["month_index"])
        print(item["google_index"])
        print(item["baidu_backlink"])
        print(item["google_backlink"])
        print(item["qihoo_index"])
        print(item["qihoo_backlink"])
        print(item["sogou_index"])
        print(item["backlink"])
        print("-" * 60)


class TopPipeline_csv(object):
    def __init__(self):
        self.f = open("网站排行.csv", "a", newline="")
        self.writer = csv.writer(self.f)
        self.writer.writerow(['标题', '排名', '百度预估流量', '百度收录', '单月收录', '谷歌收录', '百度反链数', '谷歌反链数',
                              '360收录', '360反链数', '搜狗收录', '反链数'])

    def process_item(self, item, spider):
        L = [item["title"], item["rank"], item["baidu_flow"], item["baidu_index"], item["month_index"],
             item["google_index"], item["baidu_backlink"], item["google_backlink"], item["qihoo_index"],
             item["qihoo_backlink"], item["sogou_index"], item["backlink"]]
        self.writer.writerow(L)
        return item


class TopPipeline_sql(object):
    def __init__(self):
        self.db = pymysql.connect(host="localhost", user="root", password="102030", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        c_db = "create database if not exists chinaz character set utf8"
        u_db = "use chinaz"
        c_tab = "create table if not exists chinaz(title varchar(255)," \
                "rank varchar(255)," \
                "baidu_flow varchar(255)," \
                "baidu_index varchar(255)," \
                "month_index varchar(255)," \
                "google_index varchar(255)," \
                "baidu_backlink varchar(255)," \
                "google_backlink varchar(255)," \
                "qihoo_index varchar(255)," \
                "qihoo_backlink varchar(255)," \
                "sogou_index varchar(255)," \
                "backlink varchar(255)" \
                ")charset=utf8"
        warnings.filterwarnings("ignore")
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_tab)
        except Warning:
            pass
        ins = "insert into chinaz(title,rank,baidu_flow,baidu_index,month_index,google_index,baidu_backlink," \
              "google_backlink,qihoo_index,qihoo_backlink,sogou_index,backlink) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        L = [item["title"], item["rank"], item["baidu_flow"], item["baidu_index"], item["month_index"],
             item["google_index"], item["baidu_backlink"], item["google_backlink"], item["qihoo_index"],
             item["qihoo_backlink"], item["sogou_index"], item["backlink"]]
        self.cursor.execute(ins, L)
        self.db.commit()
