# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from __future__ import absolute_import
from itemadapter import ItemAdapter
import json
import sys
#from celery_app.tasks import *
from .tasks import add_item
from scrapy.utils.serialize import ScrapyJSONEncoder
_encoder = ScrapyJSONEncoder()

class CrawlerAppPipeline:
    def process_item(self, item, spider):
        add_item.delay(_encoder.encode(item))
        return item
