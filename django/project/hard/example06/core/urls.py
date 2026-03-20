from django.urls import path

from .views import admin_page, create_employee, employee_list, export_employees, export_page, reports

urlpatterns = [
    path("employees/export/", export_employees, name="export_employees"),
    path("employees/create/", create_employee, name="create_employee"),
    path("employees/", employee_list, name="employee_list"),
    path("reports/", reports, name="reports"),
    path("export-page/", export_page, name="export_page"),
    path("admin-page/", admin_page, name="admin_page"),
]
