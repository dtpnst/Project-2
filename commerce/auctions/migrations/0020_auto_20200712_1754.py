# Generated by Django 3.0.7 on 2020-07-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_auto_20200712_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_listing',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user_bid',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=19),
            preserve_default=False,
        ),
    ]
