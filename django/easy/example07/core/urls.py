from django.urls import path
from .views import feedback, feedback_list

urlpatterns = [
    path("feedback/", feedback, name="feedback"),
    path("feedbacks/", feedback_list, name="feedback_list"),
]
