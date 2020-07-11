from rest_framework import serializers
from .models import *
from django.http import JsonResponse, HttpResponse

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"


class SubscribeListSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()

    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'profile']

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user   
    pass