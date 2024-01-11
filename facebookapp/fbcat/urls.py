from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('cat/', category, name='cat'),
    path('finfo/', finfo, name='furinf'),
    path('about/', about, name='about'),
    path('login/', log_in, name='log_in'),
]