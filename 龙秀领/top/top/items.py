# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    rank = scrapy.Field()
    baidu_flow = scrapy.Field()
    baidu_index = scrapy.Field()
    month_index = scrapy.Field()
    google_index = scrapy.Field()
    baidu_backlink = scrapy.Field()
    google_backlink = scrapy.Field()
    qihoo_index = scrapy.Field()
    qihoo_backlink = scrapy.Field()
    sogou_index = scrapy.Field()
    backlink = scrapy.Field()
