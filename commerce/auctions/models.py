from django.contrib.auth.models import AbstractUser
from django.db import models


class Auction_Listing(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    starting_bid = models.DecimalField(max_digits=19, decimal_places=2)
    current_bid = models.ForeignKey(
        'Bid',
        on_delete=models.SET_NULL,
        null=True
    )
    img_url = models.CharField(max_length=256, blank=True)
    listing_category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True
    )
    seller = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        null=True
    )
    active = models.BooleanField(default=True)
    def __str__(self):
        return f"Title: {self.title} and Description: {self.description} and Starting Bid: {self.starting_bid} and Category: {self.listing_category.name}"


class User(AbstractUser):
    watchlist = models.ManyToManyField(Auction_Listing, blank=True, related_name="watching")


class Bid(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        null=True
    )
    user_bid = models.DecimalField(max_digits=19, decimal_places=2)


class Comment(models.Model):
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        null=True
    )
    user_comment = models.CharField(max_length=256, null=True)
    auction_listing = models.ForeignKey(
        'Auction_Listing',
        on_delete=models.CASCADE,
        null=True
    )

class Category(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return f"{self.name}"