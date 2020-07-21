from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
import json
from .models import *
# Create your views here.


from auth_app.models import *
from rest_framework import generics
from .serializers import *
import json
from rest_framework.decorators import api_view
from rest_framework import serializers
# Create your views here.


class UserSubscribeCreateView(generics.CreateAPIView):
    serializer_class = UserSubscribeSerializer
    def post(self, request, *args, **kwargs):
        print("view ", request.data)
        ser = UserSubscribeSerializer(data=request.data);
        if ser.is_valid() is False:
            return JsonResponse({"message":ser.errors}, status=401)
            
        if ser.save() is None:
            return JsonResponse({"message":ser.errors}, status=401)
     
        return JsonResponse({"message":"ok"}, status=201)

class SubscribeListView(generics.ListAPIView):
    serializer_class = SubscribeSerializer

    def get(self, request):
        subscribes = Subscribe.objects.all()

        ser = SubscribeSerializer(subscribes, many=True)

        return JsonResponse(ser.data, status=200, safe=False) 

class UserSubscribeFetchView(generics.ListAPIView):
    serializer_class = UserSubscribeModelSerializer
    def get_queryset(self, authorizaton):
        auth = Auth.objects.filter(token=authorizaton).first()

        if auth is None:
            return None
        print(auth.id)
        user = User.objects.get(auth_id=auth.id)
        return Auth_Subscribe.objects.filter(user=user.id)

    def get(self, request):

        if 'Authorization' in request.headers.keys():
            user_auth = self.get_queryset(request.headers['Authorization'])
        else:
            return JsonResponse({"message":"empty token"}, status=401)
        if user_auth is None:
            return JsonResponse({"message": "first of all, you have to register your token"})
        ser = UserSubscribeModelSerializer(user_auth, many=True)

        return JsonResponse(ser.data, status=200, safe=False)
   
