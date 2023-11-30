import django.contrib
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path('index/about/contacts', contacts, name='contacts'),
    re_path('index/about', about, name='about'),
    path('login', login, name='login'),
    path('index', index, name='index'),
    path('client/<int:id>/', client, name='client'),
    # path('clients/', clients, name='clients')
]
