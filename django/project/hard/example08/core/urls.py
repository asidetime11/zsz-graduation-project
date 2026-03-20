from django.urls import path

from .views import export_users, login_page, user_detail, user_list, user_login

urlpatterns = [
    path("users/user_id_path/", user_detail, name="user_detail"),
    path("users/", user_list, name="user_list"),
    path("users/login/", user_login, name="user_login"),
    path("export/", export_users, name="export_users"),
    path("login/", login_page, name="login_page"),
]
