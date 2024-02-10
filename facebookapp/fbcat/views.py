from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseNotFound
from .models import facebook, Category, TagPost
db_fb=[
    {"title":"Головна сторінка", "url":"home"},
    {"title":"про сайт", "url":"about"},
    {"title":"додаткова інформація", "url":"furinf"},
    {"title":"категорії", "url":"cat"},
    {"title":"увійти", "url":"log_in"},
    {"title":"теги", "url":"tag_path"},
]

db_fb2=facebook.objects.all()

cat_db=Category.objects.all()

tag_db=TagPost.objects.all()
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
        "DB_fb":db_fb2,
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
        "tags":w,
    }
    return render(request, 'fbcat/profile.html', context=context)

def tag(request):
    context={
        "title":"tags",
        "tag_db":tag_db,
    }
    return render(request, "fbcat/tag.html", context=context)

def tag_tag_slug(request, tag_slug):
    w=get_object_or_404(TagPost, slug=tag_slug)
    post=w.tags.filter(is_published=facebook.STATUS.PUBLISHED)
    context = {
        "title":w.name,
        "tag_slug":tag_slug,
        "post":post,
    }
    return render(request, "fbcat/tag+tag_slug.html", context=context)

def pagenotfound(request,exception):
    return HttpResponseNotFound("Page not found")

