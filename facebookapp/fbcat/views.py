from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseNotFound
from .models import facebook, Category
db_fb=[
    {"title":"home page", "url":"home"},
    {"title":"about site", "url":"about"},
    {"title":"further information", "url":"furinf"},
    {"title":"categories", "url":"cat"},
    {"title":"log in", "url":"log_in"},
]

db_fb2=facebook.objects.all()

cat_db=Category.objects.all()

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

def dis_category(request, cat_slug):
    w=get_object_or_404(Category, slug=cat_slug)
    context={
        "title":w.name,
        "cat_slug":cat_slug,
        "db":db_fb2,
    }
    return render(request, "fbcat/dis_cat.html", context=context)

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

def profile(request, pro_slug):
    w=get_object_or_404(facebook, slug=pro_slug)
    context={
        "title":"@"+f"{w.title}",
        "pro_slug":pro_slug,
        "DB_fb":db_fb2,
    }
    return render(request, 'fbcat/profile.html', context=context)

def pagenotfound(request,exception):
    return HttpResponseNotFound("Page not found")

