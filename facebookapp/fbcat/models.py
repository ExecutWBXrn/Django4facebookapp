from django.db import models
from django.urls import reverse


class facebook(models.Model):
    title = models.CharField(max_length=255)
    describe = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"\ntitle:{self.title}\ndescribe:{self.describe}\n"

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pro_slug":self.slug})