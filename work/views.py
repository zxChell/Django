from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
data = {
    'study': 'Alabuga',
    'group': '3326А',
    'speciality': 'Fronted',
    'release': 'Fronted Medium developer',
    'fullname': 'Chunchukov Arsenii Ivanovich',
    'height': 183,
    'weight': 60,
    'number_phone': 89127018780,
    'social_network': '@ZxckuRve',
}


def header(request):
    return render(request, 'header.html')


def index(request):
    return render(request, 'index.html', context=data)


def about(request):
    return render(request, 'about.html', context=data)


def contacts(request):
    return render(request, 'contacts.html', context=data)