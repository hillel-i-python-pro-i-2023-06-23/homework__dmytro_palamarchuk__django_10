"""Url pattern"""
from django.urls import path
from . import views

APP_NAME = "base"

urlpatterns = [
    path("", views.hello_world, name='hello_world'),
]
