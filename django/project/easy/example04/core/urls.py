from django.urls import path
from .views import subscribe, subscriber_list

urlpatterns = [
    path("subscribe/", subscribe, name="subscribe"),
    path("subscribers/", subscriber_list, name="subscriber_list"),
]
