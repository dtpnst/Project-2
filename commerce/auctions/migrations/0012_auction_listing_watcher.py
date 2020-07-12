# Generated by Django 3.0.7 on 2020-07-11 21:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200711_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='watcher',
            field=models.ManyToManyField(blank=True, related_name='watchers', to=settings.AUTH_USER_MODEL),
        ),
    ]
