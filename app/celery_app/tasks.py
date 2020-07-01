from celery import shared_task
from app.celery import app
import time
import json

@shared_task
def celery_task(counter):
    email = "hassanzadeh.sd@gmail.com"
    time.sleep(3)
    return '{} Done!'.format(counter)


@app.task(name='celery_app.tasks.add_item')
def add_item(item):
    item = json.loads(item)
    print(item)

    return '1'