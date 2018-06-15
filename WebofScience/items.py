# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaperDataItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    journal = scrapy.Field()
    ISSN = scrapy.Field()
    doc_type = scrapy.Field()
    author = scrapy.Field()
    address = scrapy.Field()
    correspond_adds=scrapy.Field()
    # url = scrapy.Field()
