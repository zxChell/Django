from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


clients = [
    {'id': 1, 'name': 'Tom', 'lang': 'Python'},
    {'id': 2, 'name': 'Tom', 'lang': 'JavaScript'},
    {'id': 3, 'name': 'Tom', 'lang': 'C#'},
    {'id': 4, 'name': 'Tom', 'lang': 'C++'},
]


def login(request):
    return HttpResponse(f'432423')


def index(request):
    header = 'Данные пользователя'
    langs = ['Python', 'C++', 'C#', 'JavaScript']
    user = {'name': 'Andrey', 'age': 18}
    address = ('sdgfdsgsd', 13, 228)
    text = '<p>My text</p>'
    data = {'header': header, 'langs': langs, 'user': user, 'address': address, 'text': text, 'id': id}
    return render(request, 'index.html', context=data)
    # return render(request, 'index.html', context={'person': Person('Tom')})


def about(request):
    return render(request, 'about.html', context={'clients': clients})


def contacts(request):
    return render(request, 'contacts.html', context={'clients': clients})


def client(request, id):
    return render(request, 'client.html', context={'id': id})


