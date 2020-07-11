from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
import json
from .models import *
# Create your views here.

@api_view(['POST'])
def update_subscribe(request):
    auth = request.headers.get('Authorization')

    if auth is None:
        return JsonResponse({"message":"token is empty"}, status=401)

    if body is not None:
        body = json.loads(request.body)
        
        Auth_Subscribe.objects.create
    
            
    return JsonResponse({"message":"ok"}, status=200)

    