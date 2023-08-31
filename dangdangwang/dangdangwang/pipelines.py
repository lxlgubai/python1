# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class dangdangwangPipeline(object):
    def __init__(self):
        self.f = open("ddw.csv","a",newline="")
        # 设置文件第一行的字段名，注意要跟spider传过来的字典key名称相同
        self.fieldnames = ["bt","sj","dj","zk","s_time","press","plrs","tj","dzs"]
        # 指定文件的写入方式为csv字典写入，参数1为指定具体文件，参数2为指定字段名
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        # 写入第一行字段名，因为只要写入一次，所以文件放在__init__里面
        self.writer.writeheader()
    def process_item(self, item, spider):
        # 写入spider传过来的具体数值
        self.writer.writerow(item)
        return item
    def close(self,spider):
        self.f.close()