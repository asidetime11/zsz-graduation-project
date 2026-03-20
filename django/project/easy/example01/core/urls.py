from django.urls import path

from .views import register_view, user_list_view

urlpatterns = [
    path("register/", register_view, name="register"),
    path("users/", user_list_view, name="user_list"),
]
