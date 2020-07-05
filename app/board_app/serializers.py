from rest_framework import serializers
from .models import Posts, Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['url', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    url = UrlSerializer()
    
    class Meta:
        model = Posts
        fields = ['title', 'url', 'updated_at']

