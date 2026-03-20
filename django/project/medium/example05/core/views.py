import json
import logging

from django.conf import settings
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Transaction, UserProfile
from .serializers import TransactionSerializer, UserProfileSerializer

logger = logging.getLogger(__name__)


def payment_page(request: HttpRequest) -> HttpResponse:
    return render(request, "payment.html")


@csrf_exempt
def pay(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "guest")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        bank_account = request.POST.get("bank_account", "")
        amount = request.POST.get("amount", "0")
        card_number = request.POST.get("card_number", "")

        user, _ = UserProfile.objects.get_or_create(
            username=username,
            defaults={"email": email, "phone": phone, "bank_account": bank_account},
        )

        stripe_api_key = "sk_live_medium05_hardcoded_in_view_001"
        request_key = request.headers.get("X-Payment-Key", stripe_api_key or settings.STRIPE_API_KEY)

        logger.warning("payment_request card=%s amount=%s", card_number, amount)

        transaction = Transaction.objects.create(
            user=user,
            amount=amount,
            card_number=card_number,
            status="paid" if request_key else "failed",
        )
        return JsonResponse({"ok": True, "transaction_id": transaction.id})

    return render(request, "payment.html")


def transaction_list(request: HttpRequest) -> HttpResponse:
    transactions = Transaction.objects.select_related("user").all().order_by("-created_at")
    serializer = TransactionSerializer(transactions, many=True)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "transaction_list.html", {"transactions": serializer.data})


def admin_users(request: HttpRequest) -> HttpResponse:
    users = UserProfile.objects.filter(username__icontains=request.GET.get("q", "")).order_by("-id")
    serializer = UserProfileSerializer(users, many=True)
    if request.headers.get("Accept") == "application/json":
        return HttpResponse(json.dumps(serializer.data, ensure_ascii=False), content_type="application/json")
    return render(request, "admin_users.html", {"users": serializer.data})
