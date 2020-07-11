from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction_Listings(models.Model):
    AVAILABLE = 'AV'
    SOLD = 'SO'
    CATEGORY_CHOICES = [('Available')]

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    starting_bid = models.IntegerField()
    img_url = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"Title: {self.title} and Description: {self.description} and Starting Bid: {self.starting_bid} Image: {self.img_url}"

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass