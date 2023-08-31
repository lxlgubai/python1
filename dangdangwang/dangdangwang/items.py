# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangwangItem(scrapy.Item):
    # define the fields for your item here like:

    bt = scrapy.Field()
    sj = scrapy.Field()
    dj = scrapy.Field()
    zk = scrapy.Field()
    s_time = scrapy.Field()
    press = scrapy.Field()
    plrs = scrapy.Field()
    tj = scrapy.Field()
    dzs = scrapy.Field()
