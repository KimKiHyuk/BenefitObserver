from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'celery_app'

urlpatterns = [
    path('async/notice/', views.sync_notices),
    path('async/log/', views.get_log)
]