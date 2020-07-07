# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crawler_app.settings import app

from itemadapter import ItemAdapter
import json

import logging
logger = logging.getLogger(__name__)

class CrawlerAppPipeline:
    def process_item(self, item, spider):
        app.send_task('celery_app.crawler.sw', kwargs={'data': item.__dict__['_values']})
        return item
