# Generated by Django 3.1 on 2020-08-27 17:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_auto_20200826_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='thumbs_up',
        ),
        migrations.AddField(
            model_name='event',
            name='save_event',
            field=models.ManyToManyField(blank=True, related_name='save_event', to=settings.AUTH_USER_MODEL),
        ),
    ]
