from django.contrib import admin
from django.urls import path, re_path
from chunchukov_app import views

urlpatterns = [
    re_path(r'full_name/about/contact/', views.contact, kwargs={'github': 'https://github.com/zxChell', 'number': 89127018780, 'telegram': '@ZxckuRve'}),
    re_path(r'full_name/about/', views.about, kwargs={'city': 'Kirov', 'up': 3.80, 'love': 'Люблю учиться новому'}),
    path(r'full_name/', views.full_name, kwargs={'name': 'Chunchukov Arsenii Ivanovich', 'age': 17, 'interests': 'Python'}),
    path(r'about/', views.about, kwargs={'city': 'Kirov', 'up': 3.80, 'love': 'Люблю учиться новому'}),
    path(r'contact/', views.contact, kwargs={'github': 'https://github.com/zxChell', 'number': 89127018780, 'telegram': '@ZxckuRve'})
    # path('admin/', admin.site.urls), #superuser
]

# re_path
# path
# include