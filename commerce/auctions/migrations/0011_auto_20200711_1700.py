# Generated by Django 3.0.7 on 2020-07-11 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200711_1646'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auction_Listings',
            new_name='Auction_Listing',
        ),
        migrations.RenameModel(
            old_name='Bids',
            new_name='Bid',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]