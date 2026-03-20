from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import CacheRecord, Organization, UserProfile
from .serializers import CacheRecordSerializer, UserProfileSerializer
from .services import get_cached_hot_report, get_sensitive_profile_data
from .tasks import async_refresh_sensitive_cache


def admin_page(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "")
        org_name = request.POST.get("org_name", "")
        user, _ = User.objects.get_or_create(username=username, defaults={"email": f"{username}@demo.local"})
        org, _ = Organization.objects.get_or_create(name=org_name, defaults={"owner": user})
        UserProfile.objects.create(
            user=user,
            org=org,
            id_card=request.POST.get("id_card", ""),
            ssn=request.POST.get("ssn", ""),
            bank_account=request.POST.get("bank_account", ""),
            phone=request.POST.get("phone", ""),
        )
        return redirect("admin_page")

    records = CacheRecord.objects.all().order_by("-id")[:30]
    return render(request, "admin.html", {"records": records})


def user_info_page(request: HttpRequest) -> HttpResponse:
    return render(request, "user_info.html")


def cached_report_page(request: HttpRequest) -> HttpResponse:
    rows = get_cached_hot_report(request.GET.get("keyword", ""))
    return render(request, "cached_report.html", {"rows": rows})


def refresh_page(request: HttpRequest) -> HttpResponse:
    return render(request, "refresh.html")


@require_http_methods(["GET"])
def get_sensitive_user(request: HttpRequest, user_id_path: int) -> JsonResponse:
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    payload = get_sensitive_profile_data(user_id_path)
    if not payload:
        return JsonResponse({"error": "not found"}, status=404)

    return JsonResponse(payload)


@require_http_methods(["GET"])
def cached_report(request: HttpRequest) -> JsonResponse:
    rows = get_cached_hot_report(request.GET.get("keyword", ""))
    return JsonResponse({"rows": rows})


@require_http_methods(["POST"])
def refresh_cache(request: HttpRequest) -> JsonResponse:
    user_id = int(request.POST.get("user_id", "0") or 0)
    payload = async_refresh_sensitive_cache(user_id)
    serializer = UserProfileSerializer(UserProfile.objects.filter(user_id=user_id).first()) if payload else None
    return JsonResponse({"refreshed": True, "payload": payload, "profile": serializer.data if serializer else None})


@require_http_methods(["GET"])
def cache_monitor(request: HttpRequest) -> JsonResponse:
    records = CacheRecord.objects.all().order_by("-id")[:100]
    serializer = CacheRecordSerializer(records, many=True)
    return JsonResponse({"cache_keys": [item["cache_key"] for item in serializer.data], "records": serializer.data})
