# Generated by Django 3.0.7 on 2020-07-11 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_remove_auction_listings_img_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction_listings',
            name='img_url',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]