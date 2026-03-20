from django.urls import path

from .views import activities, delete_user, stats, track, user_manage

urlpatterns = [
    path("", stats, name="stats_home"),
    path("track/", track, name="track"),
    path("activities/", activities, name="activities"),
    path("users/manage/", user_manage, name="user_manage"),
    path("users/<int:user_id_path>/", delete_user, name="delete_user"),
    path("stats/", stats, name="stats"),
]
