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
        # �����ļ���һ�е��ֶ�����ע��Ҫ��spider���������ֵ�key������ͬ
        self.fieldnames = ["bt","sj","dj","zk","s_time","press","plrs","tj","dzs"]
        # ָ���ļ���д�뷽ʽΪcsv�ֵ�д�룬����1Ϊָ�������ļ�������2Ϊָ���ֶ���
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        # д���һ���ֶ�������ΪֻҪд��һ�Σ������ļ�����__init__����
        self.writer.writeheader()
    def process_item(self, item, spider):
        # д��spider�������ľ�����ֵ
        self.writer.writerow(item)
        return item
    def close(self,spider):
        self.f.close()