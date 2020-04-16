# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsdatasetItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()

class PolitikNewsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    # location = scrapy.Field()

class HukumNewsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    # location = scrapy.Field()

class EkonomiNewsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    # location = scrapy.Field()

class KesehatanNewsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    # location = scrapy.Field()

class TeknologiNewsItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    date = scrapy.Field()
    source = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    # location = scrapy.Field()