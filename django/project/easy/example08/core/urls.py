from django.urls import path
from .views import create_ticket, ticket_list

urlpatterns = [
    path("ticket/create/", create_ticket, name="create_ticket"),
    path("tickets/", ticket_list, name="ticket_list"),
]
