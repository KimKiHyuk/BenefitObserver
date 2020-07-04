import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import json
from crawler_app.crawler_app.settings import channel, celery_instance

@celery_instance.task(name='celery_app.tasks.add_item')

def add_item(item):
    channel.basic_publish(exchange='', routing_key='crawler', body=item)
    return 'OK'