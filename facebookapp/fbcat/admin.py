from django.contrib import admin
from .models import *

@admin.register(facebook)
class AdminFacebook(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'time_update', 'is_published', 'cat']
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    list_per_page = 5
    ordering = ['time_update', 'title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_display_links = ["id", "name"]
    list_per_page = 5
    ordering = ["id"]