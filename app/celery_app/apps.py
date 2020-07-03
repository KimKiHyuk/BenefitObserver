from django.apps import AppConfig
from django.db import models
import pika
import json
from datetime import datetime
from multiprocessing import Process


def callback(ch, method, properties, body):
    from celery_app.models import CrawlerTask
    
    loads = json.loads(body)
    print(loads)
    mid = CrawlerTask(
        log=loads['log'],
        done_at=loads['timestamp']
    )
    
    mid.save()

def initalize():
    connection = pika.BlockingConnection(pika.URLParameters(broker_info))
    channel = connection.channel()
    channel.queue_declare(queue='crawler')
    channel.basic_consume(queue='crawler', auto_ack=True, on_message_callback=callback)
    channel.start_consuming()


class CeleryAppConfig(AppConfig):
    name = 'celery_app'


    def ready(self):
        print('go')
        Process(target=initalize).start()
        

