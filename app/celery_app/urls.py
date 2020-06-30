from django.urls import path

from . import views

app_name = 'worker'

urlpatterns = [
    path('sync_notices/', views.sync_notices),
]