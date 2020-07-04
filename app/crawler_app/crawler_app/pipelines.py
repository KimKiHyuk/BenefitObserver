# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from __future__ import absolute_import
import os, sys
directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("/home/key/repository/BenefitObserver/app/crawler_app/crawler_app")
from itemadapter import ItemAdapter
import json
#from celery_app.tasks import *
from scrapy.utils.serialize import ScrapyJSONEncoder
_encoder = ScrapyJSONEncoder()
print('fuckung', os.getcwd())
from tasks import add_item

class CrawlerAppPipeline:
    def process_item(self, item, spider):
        add_item.delay(_encoder.encode(item))
        return item
