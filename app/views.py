from django.shortcuts import render
from django.http import HttpResponse
# from .forms import UserForm

# Create your views here.

def index(request):
    return render (request, 'app/static/templates/login.html')

def postuser(request):
    

