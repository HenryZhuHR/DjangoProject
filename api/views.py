from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    print(type(request))
    msg="Hello, world. You're at the polls index.\n"
    
    return HttpResponse(msg)