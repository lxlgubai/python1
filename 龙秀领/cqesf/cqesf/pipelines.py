# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CqesfPipeline:
    def process_item(self, item, spider):
        print("=" * 100)
        print(item['title'])  #
        print(item['address'])  #
        print(item['address_perimeter'])  #
        print(item['Building_information'])  #
        print(item['Price'])  #
        print(item['data_price'])  #
