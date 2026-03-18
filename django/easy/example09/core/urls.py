from django.urls import path
from .views import claim, record_list

urlpatterns = [
    path("coupon/claim/", claim, name="claim"),
    path("coupons/", record_list, name="record_list"),
]
