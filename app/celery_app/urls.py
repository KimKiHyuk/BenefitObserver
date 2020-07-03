from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'celery_app'

urlpatterns = [
    path('sync_notices/', views.sync_notices),
    url(r'^get_job_log/$', views.get_log)
]