# Generated by Django 3.0.7 on 2020-07-12 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auction_listing_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auction_listing',
            old_name='status',
            new_name='active',
        ),
    ]