from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
import json
from .models import *
# Create your views here.


from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from .serializers import *
import json
from rest_framework.decorators import api_view
from rest_framework import serializers
# Create your views here.


class UserSubscribeCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        print("view ", request.data)
        ser = UserSubscribeSerializer(data=request.data);
        if ser.is_valid() is False:
            return JsonResponse({"message":ser.errors}, status=401)
            
        if ser.save() is None:
            return JsonResponse({"message":ser.errors}, status=401)
     
        return JsonResponse({"message":"ok"}, status=201)
 
    def get_serializer_class(self):
        return UserSubscribeSerializer

class UserSubscribeFetchView(generics.ListAPIView):
    serializer_class = UserSubscribeSerializer
    def get_queryset(self):
        user = self.kwargs['token']

        return Auth_Subscribe.objects.filter(user=user)

    def get(self, request, token):
        user_auth = self.get_queryset()
        print(user_auth)

        ser = UserSubscribeSerializer(user_auth, many=True)
        
        return JsonResponse(ser.data, status=200, safe=False)
   
