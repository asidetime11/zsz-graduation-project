from django.urls import path

from .views import add_payment, checkout, payment_list, payment_search

urlpatterns = [
    path("payment/add/", add_payment, name="add_payment"),
    path("payments/", payment_list, name="payment_list"),
    path("payment/search/", payment_search, name="payment_search"),
    path("checkout/", checkout, name="checkout"),
]
