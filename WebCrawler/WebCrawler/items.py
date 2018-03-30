# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UserItem(WebcrawlerItem):
    # id = scrapy.Field()
    url_token = scrapy.Field()
    name = scrapy.Field()
    uid = scrapy.Field()
    follower_count = scrapy.Field()
    answer_count = scrapy.Field()