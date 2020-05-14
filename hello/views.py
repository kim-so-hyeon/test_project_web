from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! & Hello ssoja~ Have a nice day!")
# Create your views here.
