from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse

from .models import User, Auction_Listing, Bid

class NewListingForm(forms.Form):
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    starting_bid = forms.IntegerField()
    img_url = forms.CharField(label="Image_URL (optional)", required=False)
    category = forms.CharField(label="Category (optional)", required=False)

class AddToWatchListForm(forms.Form):
    listing_id = forms.CharField(label="Listing Id")

class NewBidForm(forms.Form):
    listing_id = forms.CharField(label="Listing Id")
    bid_amount = forms.IntegerField()

class CloseAuctionForm(forms.Form):
    listing_id = forms.CharField(label="listing Id")


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Auction_Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create(request):
    if request.method == "POST":

        # Create new listing
        form = NewListingForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            img_url = form.cleaned_data["img_url"]
            category = form.cleaned_data["category"]

            # Add new listing to DB
            listing = Auction_Listing(
                title=title, description=description, 
                starting_bid=starting_bid, img_url=img_url, 
                category=category, seller=request.user)
            listing.save()

    return render(request, "auctions/create.html", {
        "form": NewListingForm()
    })


def listing(request, listing_id):
    listing = Auction_Listing.objects.get(id=listing_id)
    user = request.user
    inWatchList = False

    # Check if item is in User's watchlist
    if listing in user.watchlist.all():
        inWatchList = True
    
    minBid = listing.starting_bid
    # Add comment here
    if listing.current_bid:
        minBid = listing.current_bid.user_bid

    isSeller = False
    # Check if logged in user is the owner
    if user == listing.seller:
        isSeller = True

    isClose = False
    if not listing.active:
        isClose = True

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "inWatchList": inWatchList,
        "minBid": minBid,
        "isSeller": isSeller,
        "isClose": isClose
    })


def watchlist(request):
    if request.method == "POST":
        form = AddToWatchListForm(request.POST)
        if form.is_valid():
            listing_id = form.cleaned_data["listing_id"]
            user = request.user
            listing = Auction_Listing.objects.get(id=listing_id)

            # User able to add or remove item to or from their watchlist
            if listing in user.watchlist.all():
                user.watchlist.remove(listing)
            else:
                user.watchlist.add(listing)
            user.save()

    return render(request, "auctions/watchlist.html", {
        "watchlist": request.user.watchlist.all()
    })


def makeBid(request, listing_id):
    if request.method == "POST":
        form = NewBidForm(request.POST)
        if form.is_valid():
            listing_id = form.cleaned_data["listing_id"]
            user = request.user
            listing = Auction_Listing.objects.get(id=listing_id)
            bid_amount = form.cleaned_data["bid_amount"]

            # Only accept bid higher than starting bid
            if bid_amount > listing.starting_bid:
                bid = Bid(user=user, user_bid=bid_amount)
                bid.save()
                
                listing.current_bid = bid
                listing.save()

    return redirect('listing', listing_id=listing_id)


def closeAuction(request, listing_id):
    if request.method == "POST":
        form = CloseAuctionForm(request.POST)
        if form.is_valid():
            listing_id = form.cleaned_data["listing_id"]
            listing = Auction_Listing.objects.get(id=listing_id)

            if request.user == listing.seller:
                listing.active = False
                listing.save()

            else:
                return render(request, "auctions/error.html")

    return redirect('listing', listing_id=listing_id)

def categories(request):
    return render(request, "auctions/categories.html")