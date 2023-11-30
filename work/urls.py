import django.contrib
from django.urls import path, include, re_path
from work.views import *

urlpatterns = [
    path('about', about, name='about'),
    path('index', index, name='index'),
]
