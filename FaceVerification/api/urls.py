from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.HelloAPIView.as_view(), name='hello-view')
]
