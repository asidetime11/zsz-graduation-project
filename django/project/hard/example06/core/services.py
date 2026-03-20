import csv
from io import StringIO

from django.http import HttpResponse

from .models import Employee


def export_all_employees_csv() -> HttpResponse:
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow([
        "id",
        "company_id",
        "name",
        "id_card",
        "ssn",
        "phone",
        "salary",
        "bank_account",
        "medical_info",
        "home_address",
        "created_at",
    ])

    for emp in Employee.objects.select_related("company").all().order_by("-id"):
        writer.writerow([
            emp.id,
            emp.company_id,
            emp.name,
            emp.id_card,
            emp.ssn,
            emp.phone,
            emp.salary,
            emp.bank_account,
            emp.medical_info,
            emp.home_address,
            emp.created_at,
        ])

    response = HttpResponse(output.getvalue(), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="employees_full_export.csv"'
    return response
