# Generated by Django 3.1 on 2020-08-23 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_merge_20200823_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventcomment',
            old_name='body',
            new_name='message',
        ),
    ]