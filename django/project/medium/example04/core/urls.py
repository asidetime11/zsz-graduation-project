from django.urls import path

from .views import article_detail, create_comment, user_list

urlpatterns = [
    path("", create_comment, name="add_comment_home"),
    path("comments/create/", create_comment, name="create_comment"),
    path("articles/<int:article_id_path>/", article_detail, name="article_detail"),
    path("users/", user_list, name="user_list"),
]