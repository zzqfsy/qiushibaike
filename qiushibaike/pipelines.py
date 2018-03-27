# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class QiushibaikePipeline(object):
    def process_item(self, item, spider):
        with open("items.json", 'a', encoding='utf-8') as fp:
            fp.write(json.dumps(item._values, ensure_ascii=False) + '\n')
        # return item
