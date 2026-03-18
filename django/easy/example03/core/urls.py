from django.urls import path
from .views import search_students, student_detail

urlpatterns = [
    path("students/", search_students, name="students"),
    path("students/<int:student_id>/", student_detail, name="student_detail"),
]
