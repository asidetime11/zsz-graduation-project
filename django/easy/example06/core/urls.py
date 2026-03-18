from django.urls import path
from .views import borrow, search

urlpatterns = [
    path("search/", search, name="search"),
    path("borrow/", borrow, name="borrow"),
]
