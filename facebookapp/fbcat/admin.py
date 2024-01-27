from django.contrib import admin, messages
from .models import *

@admin.register(facebook)
class AdminFacebook(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'time_update', 'is_published', 'cat', "brief_info"]
    list_display_links = ['id', 'title']
    list_editable = ['is_published']
    list_per_page = 5
    ordering = ['time_update', 'title']
    actions = ["set_published", "set_draft"]
    search_fields = ["title", "cat__name"]
    list_filter = ["cat__name", "is_published"]
    prepopulated_fields = {"slug": ("title", )}
    filter_horizontal = ["tags"]

    @admin.display(description="Коротка інформація", ordering="describe")
    def brief_info(self, facebook: facebook):
        return f"кількість символів в описі: {len(facebook.describe)}"
    @admin.action(description="set published")
    def set_published(self, request, queryset):
        q = queryset.update(is_published=facebook.STATUS.PUBLISHED)
        self.message_user(request, f"опубліковано {q} фото")

    @admin.action(description="set draft")
    def set_draft(self, request, queryset):
        q = queryset.update(is_published=facebook.STATUS.DRAFT)
        self.message_user(request, f"деопубліковано {q} фото", messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug"]
    list_display_links = ["id", "name"]
    list_per_page = 5
    ordering = ["id"]