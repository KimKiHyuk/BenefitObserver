# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
import json

class CrawlerAppItem(Item):
    # define the fields for your item here like:
    log = Field()
    timestamp = Field()