from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'board_app'

urlpatterns = [
    url(r'^get_notices/', views.get_notices)
]