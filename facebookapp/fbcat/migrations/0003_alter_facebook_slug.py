# Generated by Django 5.0.1 on 2024-01-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbcat', '0002_facebook_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]