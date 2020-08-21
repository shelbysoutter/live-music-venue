# Generated by Django 3.1 on 2020-08-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200819_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='cashapp_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musician',
            name='cashapp_qr',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='paypal_donation_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='musician',
            name='paypal_qr',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='venmo_qr',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]