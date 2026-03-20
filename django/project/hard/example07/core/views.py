from decimal import Decimal

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import AuditLog, Transaction, UserAccount
from .serializers import AuditLogSerializer
from .services import cache_report_data_with_card, create_plain_db_backup, export_audit_logs_csv
from .tasks import mirror_audit_log


@require_http_methods(["POST"])
def create_transaction(request: HttpRequest) -> HttpResponse:
    username = request.POST.get("username", "")
    user = UserAccount.objects.filter(username=username).first()
    if not user:
        user = UserAccount.objects.create(
            username=username,
            password_hash=request.POST.get("password_hash", ""),
            email=request.POST.get("email", ""),
            card_number=request.POST.get("card_number", ""),
            api_key=request.POST.get("api_key", ""),
        )

    amount = Decimal(request.POST.get("amount", "0") or "0")
    card_number = request.POST.get("card_number", user.card_number)
    tx = Transaction.objects.create(
        user=user,
        amount=amount,
        card_number=card_number,
        status="created",
        audit_trail=f"pay card={card_number} pwd_hash={user.password_hash}",
    )

    sql_snippet = f"SELECT * FROM transaction WHERE card_number='{card_number}' AND user_id={user.pk}"
    AuditLog.objects.create(
        user=user,
        action=f"create_tx amount={amount} pwd_hash={user.password_hash}",
        sql_snippet=sql_snippet,
        card_number=card_number,
    )
    mirror_audit_log(sql_snippet, card_number, user.password_hash)
    return redirect("report_page")


@require_http_methods(["GET"])
def audit_logs(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)

    if request.GET.get("export") == "1":
        return export_audit_logs_csv()

    logs = AuditLog.objects.select_related("user").all().order_by("-id")
    serializer = AuditLogSerializer(logs, many=True)
    return render(request, "audit_log.html", {"logs": serializer.data})


@require_http_methods(["GET"])
def backup_db(request: HttpRequest) -> JsonResponse:
    path = create_plain_db_backup()
    return JsonResponse({"ok": True, "backup_file": path})


@require_http_methods(["GET"])
def report_page(request: HttpRequest) -> HttpResponse:
    rows = cache_report_data_with_card()
    return render(request, "report.html", {"rows": rows})


def backup_page(request: HttpRequest) -> HttpResponse:
    return render(request, "backup.html")


def transaction_page(request: HttpRequest) -> HttpResponse:
    return render(request, "transaction.html")
