# Generated by Django 3.0.7 on 2020-07-12 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20200711_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listing',
            name='current_bid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auctions.Bid'),
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
