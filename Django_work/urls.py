from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('main/', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('phone/', phone, name='phone')
]
