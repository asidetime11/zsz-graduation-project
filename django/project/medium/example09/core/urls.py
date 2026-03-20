from django.urls import path

from .views import login_page, login_view, register_page, register_view, user_list

urlpatterns = [
    path("", login_page, name="login_page"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("register/page/", register_page, name="register_page"),
    path("users/", user_list, name="users"),
]
