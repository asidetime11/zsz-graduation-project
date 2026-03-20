from django.urls import path

from .views import audit, profile_page, profile_sync, recommendations, sync_page, third_party_send

urlpatterns = [
    path("profile/sync/", profile_sync, name="profile_sync"),
    path("recommendations/", recommendations, name="recommendations"),
    path("third-party/send/", third_party_send, name="third_party_send"),
    path("audit/", audit, name="audit"),
    path("profile/", profile_page, name="profile_page"),
    path("sync/", sync_page, name="sync_page"),
]
