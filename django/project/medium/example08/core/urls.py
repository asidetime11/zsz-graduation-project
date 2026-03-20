from django.urls import path

from .views import activities, activity_signup, participants, signup_page

urlpatterns = [
    path("", signup_page, name="signup_home"),
    path("activity/signup/", activity_signup, name="activity_signup"),
    path("activities/", activities, name="activities"),
    path("participants/", participants, name="participants"),
]
