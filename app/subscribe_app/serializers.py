from rest_framework import serializers
from .models import *
from auth_app.serializers import UserSerializer
from django.http import JsonResponse, HttpResponse


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = "__all__"

    def validate(self, data):
        if data.get('subscribe') is None:
            return False
        return data

    def save(self, **kwargs):
        validated_data = self.validated_data
        self.instance = self.create(validated_data)
        # or update
        return self.instance

    def create(self, validated_data):
        instance, _ = Subscribe.objects.get_or_create(validated_data['subscribe'])

        return instance


class UserSubscribeSerializer(serializers.ModelSerializer):
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
        print('save')
        users = UserSerializer(data=self.validated_data['token'])
        subscribea = SubscribeSerializer(data=self.validated_data['subscribes'])
        
        saved_user_instance = users.save()
        saved_subscribe_instance = subscribea.save()

        return self.create({"user":saved_user_instance, "subscribe" : saved_subscribe_instance})
        # or update
        #return instance

    def create(self, validated_data):

        instance, _ = Auth_Subscribe.objects.get_or_create(**validated_data)
        
        return instance
        #return user




# class SubscribeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subscribe
#         fields = "__all__"


# class SubscribeListSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'profile']

#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile')
#         user = User.objects.create(**validated_data)
#         Profile.objects.create(user=user, **profile_data)
#         return user   
#     pass