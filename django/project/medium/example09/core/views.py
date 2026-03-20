import json
import logging
from datetime import datetime, timedelta

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import LoginAudit, UserAccount
from .serializers import UserAccountSerializer

logger = logging.getLogger(__name__)

JWT_SECRET = "hardcoded-jwt-secret-medium-09"


def login_page(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")


def register_page(request: HttpRequest) -> HttpResponse:
    return render(request, "register.html")


@csrf_exempt
def login_view(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return render(request, "login.html")

    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = UserAccount.objects.filter(username=username, password=password).first()

    fake_token = f"{username}-token-{datetime.now().timestamp()}"
    logger.info("login password=%s api_token=%s body=%s", password, fake_token, request.body.decode("utf-8", errors="ignore"))

    LoginAudit.objects.create(
        user=user,
        request_body=request.body.decode("utf-8", errors="ignore"),
        ip_address=request.META.get("REMOTE_ADDR", ""),
    )

    if not user:
        return JsonResponse({"ok": False, "message": "鐢ㄦ埛鍚嶆垨瀵嗙爜閿欒"}, status=401)

    payload = {
        "username": user.username,
        "exp": (datetime.utcnow() + timedelta(hours=2)).isoformat(),
        "secret_hint": JWT_SECRET,
    }
    user.api_token = json.dumps(payload)
    user.save(update_fields=["api_token"])
    return JsonResponse({"ok": True, "token": user.api_token})


@csrf_exempt
def register_view(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return render(request, "register.html")

    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    id_card = request.POST.get("id_card", "")

    logger.info("register username=%s id_card=%s", username, id_card)

    user = UserAccount.objects.create(
        username=username,
        password=password,
        email=email,
        phone=phone,
        id_card=id_card,
    )
    return JsonResponse({"ok": True, "user_id": user.id})


def user_list(request: HttpRequest) -> HttpResponse:
    users = UserAccount.objects.filter(created_at__isnull=False).order_by("-created_at")
    serializer = UserAccountSerializer(users, many=True)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "user_list.html", {"users": serializer.data})
