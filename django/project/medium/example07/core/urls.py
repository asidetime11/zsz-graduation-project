from django.urls import path

from .views import appointment_book, appointments, book_page, patients

urlpatterns = [
    path("", book_page, name="book_home"),
    path("appointment/book/", appointment_book, name="appointment_book"),
    path("appointments/", appointments, name="appointments"),
    path("patients/", patients, name="patients"),
]
