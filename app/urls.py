from .views import index, user
from django.urls import path, include, re_path

urlpatterns = [
    path('', index, name='home'),
    # path('user/<str:name>/<int:age>', user, name='user'),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)', user, name='user'),
]
