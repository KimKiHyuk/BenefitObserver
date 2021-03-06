from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import CrawlerTask
from .serializers import CelerySerializer
from django.core.exceptions import ObjectDoesNotExist
import json
from datetime import datetime

@api_view(['POST'])
def sync_notices(request):
    # serjzer
    return HttpResponse("Done")

@api_view(['GET'])
def get_log(request):
    start_datetime = request.GET.get('start_datetime')
    end_datetime = request.GET.get('end_datetime')
    logs = None
    try:
        if start_datetime is None or end_datetime is None:
            logs = CrawlerTask.objects.all()
        else:
            logs = CrawlerTask.objects.filter(done_at__gte=start_datetime, done_at__lte=end_datetime)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    ser = CelerySerializer(logs, many=True)

    return JsonResponse(ser.data, status=200, safe=False)