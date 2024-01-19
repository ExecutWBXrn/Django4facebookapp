from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('cat/', category, name='cat'),
    path('cat/<slug:cat_slug>', dis_category, name='dcat'),
    path('finfo/', finfo, name='furinf'),
    path('about/', about, name='about'),
    path('login/', log_in, name='log_in'),
    path('profile/<slug:pro_slug>', profile, name="profile"),
    path('tag/', tag, name='tag_path'),
    path('tag/<slug:tag_slug>', tag_tag_slug, name="tag_slug_path"),
]