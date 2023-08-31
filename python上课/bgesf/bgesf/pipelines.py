# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BgesfPipeline:
    def process_item(self, item, spider):
        print("*"*50)
        print(item["url1"])
        print(item["url2"])
        print(item["url3"])
        print(item["url4"])
        print("*" * 50)
