
from django.contrib import admin
from django.urls import path, include

from siteapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
