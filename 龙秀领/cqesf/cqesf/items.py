# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CqesfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  #
    address = scrapy.Field()  #
    address_perimeter = scrapy.Field()  #
    Building_information = scrapy.Field()  #
    Price = scrapy.Field()  #
    data_price = scrapy.Field()  #
