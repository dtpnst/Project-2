from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Auction_Listings(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    starting_bid = models.IntegerField()

    def __str__(self):
        return f"Title: {self.title} and Description: {self.description} and Starting Bid: {self.starting_bid}"

class Bids(models.Model):
    pass

class Comments(models.Model):
    pass