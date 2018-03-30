# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from WebCrawler.utils.sqlutils import SQLUtils


class WebcrawlerPipeline(object):
    def process_item(self, item, spider):
        sql_helper = getattr(spider, 'sql_helper', None)
        row = sql_helper.item_to_row(item)
        if row:
            if not sql_helper.query_url_token(row):
                print '!!!'
                sql_helper.add_to_db(row)
        return item
