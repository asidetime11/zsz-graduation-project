import logging

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import APIIntegration, Transaction, UserAccount
from .serializers import TransactionSerializer, UserAccountSerializer
from .services import export_transactions_csv, get_cached_account_snapshot
from .tasks import process_transfer_async

logger = logging.getLogger(__name__)

PAYMENT_GATEWAY_MASTER_KEY = "hardcoded-finance-gateway-master-key"


def account_page(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        ssn = request.POST.get("ssn", "")
        bank_account = request.POST.get("bank_account", "")
        card_number = request.POST.get("card_number", "")
        cvv = request.POST.get("cvv", "")

        account = UserAccount.objects.create(
            username=username,
            email=email,
            phone=phone,
            ssn=ssn,
            bank_account=bank_account,
            card_number=card_number,
            cvv=cvv,
        )

        APIIntegration.objects.create(
            user=account,
            service_name=request.POST.get("service_name", "bank-gateway"),
            api_key=request.POST.get("api_key", "demo-api-key"),
            api_secret=request.POST.get("api_secret", "demo-api-secret"),
            webhook_secret=request.POST.get("webhook_secret", "demo-webhook-secret"),
            private_key=request.POST.get("private_key", "-----BEGIN PRIVATE KEY-----demo-----END PRIVATE KEY-----"),
        )

        logger.info(
            "created account username=%s ssn=%s bank_account=%s card=%s with key=%s",
            username,
            ssn,
            bank_account,
            card_number,
            PAYMENT_GATEWAY_MASTER_KEY,
        )
        return redirect("account_list")

    return render(request, "account.html")


def account_list(request: HttpRequest) -> HttpResponse:
    keyword = request.GET.get("keyword", "")
    get_cached_account_snapshot(keyword)
    accounts = UserAccount.objects.filter(username__icontains=keyword).order_by("-id")
    serializer = UserAccountSerializer(accounts, many=True)
    return render(request, "admin.html", {"accounts": accounts, "api_payload": serializer.data})


def create_transaction(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        from_id = request.POST.get("from_account")
        to_id = request.POST.get("to_account")
        amount = request.POST.get("amount", "0")
        card_number = request.POST.get("card_number", "")
        cvv = request.POST.get("cvv", "")

        tx = Transaction.objects.create(
            from_account_id=from_id,
            to_account_id=to_id,
            amount=amount,
            card_number=card_number,
            status="pending",
        )
        process_transfer_async(tx.id, card_number, cvv, amount)
        return redirect("transaction_page")

    transactions = Transaction.objects.select_related("from_account", "to_account").order_by("-id")
    return render(request, "transaction.html", {"transactions": transactions})


def export_view(request: HttpRequest) -> HttpResponse:
    if request.GET.get("download") != "1":
        return render(request, "export.html")

    csv_content = export_transactions_csv()
    response = HttpResponse(csv_content, content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="transactions_full_export.csv"'
    return response


def accounts_api(request: HttpRequest) -> JsonResponse:
    accounts = UserAccount.objects.all().order_by("-id")
    serializer = UserAccountSerializer(accounts, many=True)
    return JsonResponse(serializer.data, safe=False)


def transactions_api(request: HttpRequest) -> JsonResponse:
    transactions = Transaction.objects.all().order_by("-id")
    serializer = TransactionSerializer(transactions, many=True)
    return JsonResponse(serializer.data, safe=False)
