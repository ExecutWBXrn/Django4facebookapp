from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound

def index(request):
    return HttpResponse("Head page!")

def pagenotfound(request,exception):
    return HttpResponseNotFound("Page not found")

