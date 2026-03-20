from django.urls import path

from .views import (
    admin_page,
    cache_monitor,
    cached_report,
    cached_report_page,
    get_sensitive_user,
    refresh_cache,
    refresh_page,
    user_info_page,
)

urlpatterns = [
    path("user/<int:user_id_path>/sensitive/", get_sensitive_user, name="get_sensitive_user"),
    path("reports/cached/", cached_report, name="cached_report"),
    path("refresh/", refresh_cache, name="refresh_cache"),
    path("monitor/cache/", cache_monitor, name="cache_monitor"),
    path("user-info/", user_info_page, name="user_info_page"),
    path("cached-report/", cached_report_page, name="cached_report_page"),
    path("refresh-page/", refresh_page, name="refresh_page"),
    path("admin-page/", admin_page, name="admin_page"),
]
