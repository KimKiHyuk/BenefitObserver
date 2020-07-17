from rest_framework import serializers
from .models import *
from auth_app.serializers import UserSerializer
from django.http import JsonResponse, HttpResponse
from auth_app.models import *

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

        auth = Auth.objects.filter(token=self.validated_data['token']).first()
        print(auth, auth.id)
        user = User.objects.get(auth_id=auth.id)
        print(user, user.id)
        auth_subscribe = Auth_Subscribe.objects.filter(user=user.id)
        print('my item', auth_subscribe)

        Auth_Subscribe.objects.filter(user_id=user.id).delete()
        for subscribe in self.validated_data['subscribes']:
            try:
                subc = Subscribe.objects.get(topic=subscribe)
                instances.append(self.create({"user_id":user.id, "subscribe" : subc}))
            except:
                pass
            
        
        
        return instances

    def create(self, validated_data):
        print('last create', validated_data)
        instance, _ = Auth_Subscribe.objects.create(**validated_data)
        
        return instance
        #return user
    def update(self, validated_data):
        instance, _ = Auth_Subscribe.objects.update(**validated_data)
        
        return instance



