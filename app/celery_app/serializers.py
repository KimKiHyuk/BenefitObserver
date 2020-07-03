from rest_framework import serializers
from .models import CrawlerTask

class CelerySerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawlerTask
        fields = ['log', 'done_at']