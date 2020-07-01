from celery import Celery
import json
app = Celery('celery_app', backend='amqp', broker='amqp://key:fkdbeh41@localhost:5672/key_host')


@app.task(name='celery_app.tasks.add_item')
def add_item(item):
     item = json.loads(item)
     return item