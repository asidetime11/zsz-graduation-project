from decimal import Decimal

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import Company, Employee, PayrollTask
from .serializers import EmployeeSerializer
from .services import export_all_employees_csv
from .tasks import calculate_payroll


def admin_page(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "")
        company_name = request.POST.get("company", "")
        user, _ = User.objects.get_or_create(username=username, defaults={"email": f"{username}@demo.local"})
        company, _ = Company.objects.get_or_create(name=company_name, defaults={"admin": user})
        Employee.objects.create(
            company=company,
            name=request.POST.get("name", ""),
            id_card=request.POST.get("id_card", ""),
            ssn=request.POST.get("ssn", ""),
            phone=request.POST.get("phone", ""),
            salary=Decimal(request.POST.get("salary", "0") or "0"),
            bank_account=request.POST.get("bank_account", ""),
            medical_info=request.POST.get("medical_info", ""),
            home_address=request.POST.get("home_address", ""),
        )
        return redirect("admin_page")

    emps = Employee.objects.all().order_by("-id")
    return render(request, "admin.html", {"employees": emps})


@require_http_methods(["POST"])
def create_employee(request: HttpRequest) -> JsonResponse:
    username = request.POST.get("username", "")
    company_name = request.POST.get("company", "")
    user, _ = User.objects.get_or_create(username=username, defaults={"email": f"{username}@demo.local"})
    company, _ = Company.objects.get_or_create(name=company_name, defaults={"admin": user})

    emp = Employee.objects.create(
        company=company,
        name=request.POST.get("name", ""),
        id_card=request.POST.get("id_card", ""),
        ssn=request.POST.get("ssn", ""),
        phone=request.POST.get("phone", ""),
        salary=Decimal(request.POST.get("salary", "0") or "0"),
        bank_account=request.POST.get("bank_account", ""),
        medical_info=request.POST.get("medical_info", ""),
        home_address=request.POST.get("home_address", ""),
    )

    task = PayrollTask.objects.create(
        employee=emp,
        amount=emp.salary,
        card_number=emp.bank_account,
        status="pending",
    )
    calculate_payroll(task.pk)
    return JsonResponse({"employee_id": emp.pk, "task_id": task.pk})


@require_http_methods(["GET"])
def employee_list(request: HttpRequest) -> HttpResponse:
    emps = Employee.objects.select_related("company").all().order_by("-id")
    serializer = EmployeeSerializer(emps, many=True)
    if request.GET.get("format") == "json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "employee_list.html", {"employees": serializer.data})


@require_http_methods(["GET"])
def export_employees(request: HttpRequest) -> HttpResponse:
    return export_all_employees_csv()


@require_http_methods(["GET"])
def reports(request: HttpRequest) -> HttpResponse:
    rows = list(
        Employee.objects.values("company__name", "name", "salary", "bank_account").order_by("-salary")[:50]
    )
    return render(request, "report.html", {"rows": rows})


def export_page(request: HttpRequest) -> HttpResponse:
    return render(request, "export.html")
