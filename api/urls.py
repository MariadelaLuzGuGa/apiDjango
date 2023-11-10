"""Codigo para la URLS en la carpeta API"""
from django.urls import path
from api import views

urlpatterns = [
    path("", views.home),
]
