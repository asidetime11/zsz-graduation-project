from django.urls import path

from .views import admin_page, notifications, notifications_api, start_export, task_status

urlpatterns = [
    path("admin-page/", admin_page, name="admin_page"),
    path("export/start/", start_export, name="start_export"),
    path("export/status/<int:task_id_path>/", task_status, name="task_status"),
    path("notifications/", notifications, name="notifications"),
    path("api/notifications/", notifications_api, name="notifications_api"),
]
