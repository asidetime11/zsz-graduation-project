from django.urls import path

from .views import (
    admin_page,
    analytics_query,
    export_page,
    export_report,
    query_builder_page,
    query_history_review,
    report_list,
)

urlpatterns = [
    path("analytics/query/", analytics_query, name="analytics_query"),
    path("reports/", report_list, name="report_list"),
    path("export/", export_report, name="export_report"),
    path("admin/", admin_page, name="admin_page"),
    path("query-builder/", query_builder_page, name="query_builder_page"),
    path("export-page/", export_page, name="export_page"),
    path("history/", query_history_review, name="query_history_review"),
]
