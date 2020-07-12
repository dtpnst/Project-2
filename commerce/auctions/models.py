from django.contrib.auth.models import AbstractUser
from django.db import models


class Auction_Listing(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    starting_bid = models.IntegerField()
    current_bid = models.ForeignKey(
        'Bid',
        on_delete=models.SET_NULL,
        null=True
    )
    img_url = models.CharField(max_length=256, blank=True)
    category = models.CharField(max_length=64, blank=True)
    seller = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        null=True
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Title: {self.title} and Description: {self.description} and Starting Bid: {self.starting_bid} and Image: {self.img_url} and Category: {self.category}"


class User(AbstractUser):
    watchlist = models.ManyToManyField(Auction_Listing, blank=True, related_name="watching")


class Bid(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        null=True
    )
    user_bid = models.IntegerField(null=True)


class Comment(models.Model):
    pass