from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import generics
from .models import Auth
from .serializers import *
import json
from rest_framework.decorators import api_view
from rest_framework import serializers
# Create your views here.


class AuthUserCreateView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):

        ser = UserSerializer(data=request.data)
        if ser.is_valid() is False:
            print(ser.errors)
            return JsonResponse({"message":"user validation failed"} , status=401)
        
        transcation = ser.save()

        if transcation is None:
            return JsonResponse({"message":"auth validation failed"} , status=401)

        return JsonResponse(ser.data , status=201)

    
    def get_serializer_class(self):
        return UserSerializer



