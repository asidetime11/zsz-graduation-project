from django.urls import path

from .views import audit_logs, backup_db, backup_page, create_transaction, report_page, transaction_page

urlpatterns = [
    path("audit/logs/", audit_logs, name="audit_logs"),
    path("admin/db-backup/", backup_db, name="backup_db"),
    path("reports/", report_page, name="report_page"),
    path("transactions/", create_transaction, name="create_transaction"),
    path("audit-page/", audit_logs, name="audit_page"),
    path("backup-page/", backup_page, name="backup_page"),
    path("transaction-page/", transaction_page, name="transaction_page"),
]
