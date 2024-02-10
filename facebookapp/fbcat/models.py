from django.db import models
from django.urls import reverse


class facebook(models.Model):
    class STATUS(models.IntegerChoices):
        DRAFT = 0, "DRAFT"
        PUBLISHED = 1, "PUBLISHED"
    title = models.CharField(max_length=255, verbose_name="Фото")
    describe = models.TextField(blank=True, verbose_name="Контент")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="slug")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата публікації")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата останнього оновлення")
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), STATUS.choices)) ,default=STATUS.PUBLISHED, verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категорії')
    tags = models.ManyToManyField('TagPost',blank=True ,related_name='tags')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"\ntitle:{self.title}\ndescribe:{self.describe}\n"

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pro_slug":self.slug})

    class Meta:
        verbose_name = "Фейсбук"
        verbose_name_plural = "Фейсбук"
        ordering = ['-time_create']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорії")
    slug = models.SlugField(max_length=99, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dcat", kwargs={"cat_slug":self.slug})
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class TagPost(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_slug_path", kwargs={"tag_slug":self.slug})