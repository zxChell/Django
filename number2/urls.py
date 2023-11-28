from django.contrib import admin
from django.urls import path, include, re_path
from homework.views import error

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', include('homework.urls')),
    re_path(r'^', error, name='error'),
]
