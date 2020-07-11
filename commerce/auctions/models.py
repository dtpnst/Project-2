from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction_Listings(models.Model):
    FASHION = 'FA'
    TOYS = 'TO'
    ELECTRONICS = 'EL'
    HOME = 'HO'
    OTHER = 'OT'
    CATEGORY_CHOICES = [
        (FASHION, 'Fashion'),
        (TOYS, 'Toys'),
        (ELECTRONICS, 'Electronics'),
        (HOME, 'Home'),
        (OTHER, 'Other') 
    ]

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    starting_bid = models.IntegerField()
    img_url = models.CharField(max_length=256, blank=True)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=OTHER)

    def __str__(self):
        return f"Title: {self.title} and Description: {self.description} and Starting Bid: {self.starting_bid} Image: {self.img_url} and Category: {{ listing.category}}"

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass