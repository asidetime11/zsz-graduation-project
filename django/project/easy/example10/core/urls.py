from django.urls import path
from .views import register, visitor_list

urlpatterns = [
    path("visitor/register/", register, name="visitor_register"),
    path("visitors/", visitor_list, name="visitor_list"),
]
