from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound
from .models import facebook
db_fb=[
    {"title":"home page", "url":"home"},
    {"title":"about site", "url":"about"},
    {"title":"further information", "url":"furinf"},
    {"title":"categories", "url":"cat"},
    {"title":"log in", "url":"log_in"},
]

db_fb2=facebook.objects.all()

cat_db=[
    {"id":1, "category":"photo"},
    {"id":2, "category":"video"},
]

def index(request):
    context = {
        "title":"facebook",
        "DB_fb":db_fb2,
    }
    return render(request, 'fbcat/index.html', context=context)

def category(request):
    context = {
        "title":"facebook",
    }
    return render(request, 'fbcat/category.html', context=context)

def finfo(request):
    context = {
        "title":"facebook",
    }
    return render(request, 'fbcat/finfo.html', context=context)

def about(request):
    context = {
        "title":"facebook",
    }
    return render(request, 'fbcat/about.html', context=context)

def log_in(request):
    context = {
        "title":"facebook",
    }
    return render(request, 'fbcat/login.html', context=context)

def pagenotfound(request,exception):
    return HttpResponseNotFound("Page not found")

