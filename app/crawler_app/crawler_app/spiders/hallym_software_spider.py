import scrapy
import time
from scrapy.spiders import CrawlSpider, Rule
import logging
from datetime import datetime
from ..items import CrawlerAppItem
from scrapy import signals
from scrapy import Spider
import pika
import sys
from ..settings import connection

class HallymSoftwareSpider(CrawlSpider):
    root_url = 'https://sw.hallym.ac.kr/'
    logger = logging.getLogger(__name__)
    name = 'HallymSoftwareSpider'
    

    def start_requests(self):
        urls = [
            'https://sw.hallym.ac.kr/index.php?mp=5_1'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_item)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(HallymSoftwareSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        return spider


    def spider_opened(self, spider):
        spider.logger.info('Hallym Spider opened: %s', spider.name)

    def spider_closed(self, spider):
        spider.logger.info('Hallym Spider closed: %s', spider.name)
        if connection is not None:
            spider.logger.info('=== end stream ===')
            connection.close()

    def parse_item(self, response):
        raw_url = response.xpath('/html/body/div/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/a/@href').extract()
        raw_title = response.xpath("/html/body/div/div[3]/div[2]/div[2]/table/tbody/tr/td[2]/a/@title").extract()
        item = CrawlerAppItem()
        item['log'] = [
            {
                'url': self.root_url + url,
                'title': raw_title[idx]
            } for idx, url in enumerate(raw_url)
        ]
        item['timestamp'] = datetime.now().strftime("%H:%M:%S")

        yield item