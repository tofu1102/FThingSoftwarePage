from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("index page")

def log_on(request):
    return HttpResponse("log on page")

# Create your views here.
