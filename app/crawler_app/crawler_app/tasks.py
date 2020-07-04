import os, sys
directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("/home/key/repository/BenefitObserver/app/crawler_app/crawler_app")
import json
from settings import channel
from settings import celery_instance

@celery_instance.task(name='celery_app.tasks.add_item')
def add_item(item):
    channel.basic_publish(exchange='', routing_key='crawler', body=item)

    return 'OK'