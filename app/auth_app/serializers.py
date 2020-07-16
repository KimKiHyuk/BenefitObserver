from rest_framework import serializers
from .models import *
from django.http import JsonResponse, HttpResponse

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ['token', 'updated_at']

    def validate(self, data):
        return data

    def save(self, **kwargs):
        validated_data = self.validated_data
        self.instance = self.create(validated_data)
        # or update
        return self.instance

    def create(self, validated_data):
        instance, _ = Auth.objects.get_or_create(**validated_data)

        return instance

    
    def get_serializer_class(self):
        return AuthSerializer


class UserSerializer(serializers.ModelSerializer):
    Authorization = AuthSerializer(source='auth')
    class Meta:
        model = User
        fields = ['Authorization', 'updated_at']

    def validate(self, data):
        return data

    def save(self, **kwargs):
        auth_ser = AuthSerializer(data=self.validated_data['auth'])
        
        if auth_ser.is_valid() is False:
            print(auth_ser.errors)
            return None

        instance = auth_ser.save()
        self.create(instance)
        # or update
        return instance

    def create(self, validated_data):

        user, _ = User.objects.get_or_create(auth=validated_data)
        
        return user
        #return user

