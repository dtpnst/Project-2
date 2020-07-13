from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:category_id>", views.categorylisting, name="categorylisting"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("bid", views.makeBid, name="makeBid"),
    path("closeAuction", views.closeAuction, name="closeAuction"),
    path("addComment", views.addComment, name="addComment")
]