from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'subscribe_app'

urlpatterns = [
    path('', views.UserSubscribeCreateView.as_view()),
    path('<str:token>/', views.UserSubscribeFetchView.as_view())
]