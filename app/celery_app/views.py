from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view

from .tasks import celery_task

def celery_view(request):
    for counter in range(2):
        celery_task.delay(counter)
    return HttpResponse("FINISH PAGE LOAD")



@api_view(['POST'])
def sync_notices(request):
    # serjzer
    return HttpResponse("Done")