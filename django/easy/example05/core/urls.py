from django.urls import path
from .views import create_parcel, parcel_detail

urlpatterns = [
    path("parcel/create/", create_parcel, name="create_parcel"),
    path("parcel/<int:record_id>/", parcel_detail, name="parcel_detail"),
]
