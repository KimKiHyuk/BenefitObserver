# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from crawler_app.tasks import add_item

from itemadapter import ItemAdapter
import json


class CrawlerAppPipeline:
    def process_item(self, item, spider):
        add_item.delay(json.dumps(item.__dict__['_values']))
        return item
