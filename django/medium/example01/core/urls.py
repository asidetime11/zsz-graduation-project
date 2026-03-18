from django.urls import path

from .views import create_order, order_detail, order_list, users_api

urlpatterns = [
    path("", order_list, name="order_list"),
    path("orders/", order_list, name="order_list_page"),
    path("orders/<int:order_id_path>/", order_detail, name="order_detail"),
    path("orders/create/", create_order, name="create_order"),
    path("users/", users_api, name="users_api"),
]
