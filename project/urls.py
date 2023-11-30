import django.contrib
from django.urls import path, include
from app.views import *
from work.views import *

urlpatterns = [
    path('admin/', django.contrib.admin.site.urls),
    path('work/', include('work.urls')),
    path('', header, name='header'),
]
