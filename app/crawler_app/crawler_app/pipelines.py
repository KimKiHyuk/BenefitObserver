# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from __future__ import absolute_import
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from itemadapter import ItemAdapter
import json
#from celery_app.tasks import *
from tasks import add_item

class CrawlerAppPipeline:
    def process_item(self, item, spider):
        add_item.delay(json.dumps(item.__dict__['_values']))
        return item
