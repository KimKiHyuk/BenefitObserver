from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'board_app'

urlpatterns = [
    url(r'^notice/list/', views.get_notices)
]