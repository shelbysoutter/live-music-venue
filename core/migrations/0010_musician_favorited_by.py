# Generated by Django 3.1 on 2020-08-21 16:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_auto_20200820_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorite_musician', to=settings.AUTH_USER_MODEL),
        ),
    ]