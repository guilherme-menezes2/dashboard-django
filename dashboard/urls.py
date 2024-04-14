from django.contrib import admin
from django.urls import path
from dashboard.views import index, tempo

urlpatterns = [
    path('', index, name='index'),
    path('tempo', tempo, name='tempo'),
]