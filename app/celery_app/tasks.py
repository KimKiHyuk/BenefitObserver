from celery import shared_task
from app.celery import app
from .models import CrawlerTask
import time
import json
from celery import Celery
from celery.task import task, subtask
from datetime import date
from celery.utils.log import get_task_logger
from django.utils.dateparse import parse_date
log1 = get_task_logger(__name__)

@app.task
def push_fcm(**kwargs):
    from subscribe_app.models import Subscribe

    _all = Subscribe.objects.all()

@task(name='celery_app.crawler.sw')
def sw(**kwargs):
    from celery_app.models import CrawlerTask
    from board_app.models import Posts, Url

    CrawlerTask.objects.create(
        log=json.dumps(kwargs['data']),
    )

    for post in kwargs['data']['log']:
        url_obj, _ = Url.objects.get_or_create(
            url=post['url']
        )
        _, created = Posts.objects.get_or_create(
            title=post['title'],
            url=url_obj
        )

        if created:
            push_fcm.delay()