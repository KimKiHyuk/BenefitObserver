from rest_framework import serializers
from .models import *
from auth_app.serializers import UserSerializer
from django.http import JsonResponse, HttpResponse


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"

    def validate(self, data):
        if data.get('topic') is None:
            return False
        return data

    def save(self, **kwargs):
        validated_data = self.validated_data
        self.instance = self.create(validated_data)
        # or update
        return self.instance

    def create(self, validated_data):
        instance = Subscribe.objects.get_or_create(topic=validated_data['topic'])
        print(instance)

        return instance

class UserSubscribeSerializer(serializers.Serializer):
    token = serializers.CharField(required=True, trim_whitespace=True)
    subscribes = serializers.JSONField(required=True)
        
    class Meta:
        model = Auth_Subscribe
        fields = "__all__"

    def validate(self, data):
        print(data)
        if data.get('token') is None:
            print('token is none')
            pass

        if data.get('subscribes') is None:
            print('subscribe is none')
            pass
        return data

    def save(self, **kwargs):
        instances = []
        print('save')

        users = UserSerializer(data={"Authorization": {"token" : self.validated_data['token']}})
        if users.is_valid() is False:
            print('user', users.errors)
            return None

        for subscribe in self.validated_data['subscribes']:
            subscribe = SubscribeSerializer(data={"topic" : subscribe})
            if subscribe.is_valid() is False:
                print('subscribe', subscribe.errors)
                continue
            
            saved_user_instance = users.save()
            saved_subscribe_instance = subscribe.save()
            instances.append(self.create({"user_id":saved_user_instance.id, "subscribe" : saved_subscribe_instance}))
        
        return instances

    def create(self, validated_data):
        print('last create', validated_data)
        instance, _ = Auth_Subscribe.objects.get_or_create(**validated_data)
        
        return instance
        #return user
    def update(self, validated_data):
        instance, _ = Auth_Subscribe.objects.update(**validated_data)
        
        return instance



