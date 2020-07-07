from django.apps import AppConfig
from django.db import models
import pika
import json
from datetime import datetime
from multiprocessing import Process
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from app.settings import CELERY_BROKER_URL

def callback(ch, method, properties, body):
    from celery_app.models import CrawlerTask
    from board_app.models import Posts, Url
    
    loads = json.loads(body)

    CrawlerTask.objects.create(
        log=loads['log'],
        done_at=loads['timestamp']
    )

    for post in loads['log']:
        url_obj, created = Url.objects.get_or_create(
            url=post['url']
        )
        Posts.objects.get_or_create(
            title=post['title'],
            url=url_obj
        )
def initalize():
    connection = pika.BlockingConnection(pika.URLParameters(CELERY_BROKER_URL))
    channel = connection.channel()
    channel.queue_declare(queue='crawler')
    channel.basic_consume(queue='crawler', auto_ack=True, on_message_callback=callback)
    channel.start_consuming()


class CeleryAppConfig(AppConfig):
    name = 'celery_app'


    def ready(self):
        #Process(target=initalize).start()
        pass

