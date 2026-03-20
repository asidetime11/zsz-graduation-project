from django.urls import path

from .views import admin_users, pay, payment_page, transaction_list

urlpatterns = [
    path("", payment_page, name="payment_home"),
    path("pay/", pay, name="pay"),
    path("transactions/", transaction_list, name="transactions"),
    path("admin/users/", admin_users, name="admin_users"),
]
