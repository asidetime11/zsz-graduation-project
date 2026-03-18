from django.urls import path

from .views import admin_page, analytics_view, create_report, export_view, report_list, reports_api

urlpatterns = [
    path("reports/", report_list, name="report_list"),
    path("reports/create/", create_report, name="create_report"),
    path("analytics/", analytics_view, name="analytics"),
    path("export/", export_view, name="export"),
    path("admin-page/", admin_page, name="admin_page"),
    path("api/reports/", reports_api, name="reports_api"),
]
