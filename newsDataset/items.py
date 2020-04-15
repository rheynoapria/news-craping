# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsdatasetItem(scrapy.Item):
    # define the fields for your item here like:
    date = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    source = scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()
    pass
