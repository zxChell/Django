# from django.contrib import admin
from django.urls import path, include, re_path
# from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    re_path('main/phone/', phone, name='phone'),
]
