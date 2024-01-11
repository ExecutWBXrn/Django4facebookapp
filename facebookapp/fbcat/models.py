from django.db import models

class facebook(models.Model):
    title = models.CharField(max_length=255)
    describe = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"\ntitle:{self.title}\ndescribe:{self.describe}\n"