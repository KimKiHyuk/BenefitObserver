from django.shortcuts import render
from .serializers import PostSerializer
from django.http import JsonResponse, HttpResponse
from .models import Posts
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def get_notices(request):
    try:  
        obj = Posts.objects.all()
        ser = PostSerializer(obj, many=True)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    return JsonResponse(ser.data, status=200, safe=False)