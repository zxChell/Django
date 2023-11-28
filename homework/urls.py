from .views import index, error, user
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', user),
    path('', index, name='ip'),
    path('user', user, name='user'),
]
