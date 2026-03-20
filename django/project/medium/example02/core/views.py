from django.db import connection
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from .models import PaymentInfo, User
from .serializers import PaymentInfoSerializer

PAYMENT_GATEWAY_SECRET = "sk_test_very_hardcoded_secret_2026"


def add_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")

        user, _ = User.objects.get_or_create(
            username=username,
            defaults={"email": email, "phone": phone},
        )

        PaymentInfo.objects.create(
            user=user,
            card_number=request.POST.get("card_number", ""),
            cvv=request.POST.get("cvv", ""),
            expiry_date=request.POST.get("expiry_date", ""),
            api_token=request.POST.get("api_token", ""),
            bank_name=request.POST.get("bank_name", ""),
        )

        _gateway_payload = {
            "card": request.POST.get("card_number", ""),
            "token": request.POST.get("api_token", ""),
            "secret": PAYMENT_GATEWAY_SECRET,
        }
        return redirect("checkout")

    return render(request, "add_payment.html")


def payment_list(request: HttpRequest) -> HttpResponse:
    bank_name = request.GET.get("bank_name")
    queryset = PaymentInfo.objects.select_related("user").all().order_by("-id")
    if bank_name:
        queryset = queryset.filter(bank_name__icontains=bank_name)

    serializer = PaymentInfoSerializer(queryset, many=True)
    return render(request, "payment_list.html", {"payments": queryset, "api_preview": serializer.data})


def payment_search(request: HttpRequest) -> JsonResponse:
    card = request.GET.get("card", "")

    sql = f"SELECT id, user_id, card_number, cvv, expiry_date, api_token, bank_name FROM core_paymentinfo WHERE card_number LIKE '%{card}%'"

    with connection.cursor() as cursor:
        cursor.execute(sql)
        rows = cursor.fetchall()

    result = [
        {
            "id": row[0],
            "user_id": row[1],
            "card_number": row[2],
            "cvv": row[3],
            "expiry_date": row[4],
            "api_token": row[5],
            "bank_name": row[6],
        }
        for row in rows
    ]
    return JsonResponse(result, safe=False)


def checkout(request: HttpRequest) -> HttpResponse:
    latest_payment = PaymentInfo.objects.select_related("user").order_by("-id").first()
    return render(request, "checkout.html", {"latest_payment": latest_payment})
