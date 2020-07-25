from celery import shared_task
from app.celery import app
from .models import CrawlerTask
from subscribe_app.models import *
from subscribe_app.serializers import *
from auth_app.models import *
import time
import json
from celery import Celery
from celery.task import task, subtask
from datetime import date
from celery.utils.log import get_task_logger
from django.utils.dateparse import parse_date
from celery_app.models import CrawlerTask
from board_app.models import Posts, Url

import json
import requests

FCM_API_KEY = ""

with open('secrets.json') as f:
    secrets = json.loads(f.read())
    FCM_API_KEY += secrets['FIREBASE_KEY']

queue_subscribe_table = {
    'sw' : SubscribeSerializer(Subscribe.objects.get(topic='Software engineering')),
    'ns' : SubscribeSerializer(Subscribe.objects.get(topic='Natural science'))
}

def get_fcm_request(token, topic):
    return {
        "priority" : "high",
        "notification" : {
            "body" : "새로운 공지사항이 등록되었습니다!",
            "title": "클릭해서 새로운 공지사항을 확인하세요.",
	        #"android_channel_id": "noti_push_NEW_PLAY",
	        #"sound": "NEW_MESSAGE.wav"
        },
        "data" : {
            "click_action": "FLUTTER_NOTIFICATION_CLICK",
            "type": topic
        },
        "to" : token
    }

@app.task 
def send(token, topic):
    requests.post('https://fcm.googleapis.com/fcm/send', 
        json=get_fcm_request(token, topic), 
        headers={'Content-Type' : 'application/json', 'Authorization': FCM_API_KEY, 'Accept-Encoding': 'gzip, deflate, br'}
    )

@app.task
def push_fcm(subscribe):
    _send_target = Auth_Subscribe.objects.filter(subscribe_id=subscribe['id'])
    for target in _send_target:
        auth = Auth.objects.get(
            id=User.objects.get(id=target.user_id).auth_id
        )
        send.delay(token=auth.token, topic=subscribe['topic'])

@task(name='celery_app.crawler.sw')
def sw(**kwargs):
    is_created = False

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
            is_created = True
    
    if is_created:
        if post['url'].find('sw.hallym.ac.kr') != -1:
            push_fcm.delay(subscribe=queue_subscribe_table['sw'].data)
