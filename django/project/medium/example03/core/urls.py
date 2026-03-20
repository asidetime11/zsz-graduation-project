from django.urls import path

from .views import create_post, search_posts, user_list

urlpatterns = [
    path("", search_posts, name="search_posts"),
    path("posts/search/", search_posts, name="posts_search"),
    path("posts/create/", create_post, name="create_post"),
    path("users/", user_list, name="user_list"),
]