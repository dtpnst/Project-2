# Generated by Django 3.0.7 on 2020-07-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auction_listings_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listings',
            name='category',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
