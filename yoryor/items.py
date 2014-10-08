# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArtistItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    cover = scrapy.Field()
    songs = scrapy.Field()


class YoryorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
