from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import BehaviorProfile, ThirdPartySync, UserProfile
from .serializers import ThirdPartySyncSerializer, TransactionSerializer, UserProfileSerializer
from .services import build_sync_payload, send_payload_to_third_party
from .tasks import push_profile_snapshot


@require_http_methods(["POST"])
def profile_sync(request: HttpRequest) -> JsonResponse:
    user_id = int(request.POST.get("user_id", "0") or 0)
    endpoint = request.POST.get("endpoint", "https://ad.example.com/sync")
    triggered_by = request.POST.get("triggered_by", "system")

    result = send_payload_to_third_party(user_id=user_id, endpoint=endpoint, triggered_by=triggered_by)
    if result.get("ok"):
        push_profile_snapshot(user_id, result["payload"])
    return JsonResponse(result)


@require_http_methods(["GET"])
def recommendations(request: HttpRequest) -> HttpResponse:
    user_id = request.GET.get("user_id")
    behavior = BehaviorProfile.objects.filter(user_id=user_id).first()
    profile = UserProfile.objects.filter(user_id=user_id).first()
    if not behavior or not profile:
        return HttpResponse("Not Found", status=404)

    recommendation_tags = {
        "financial_segment": behavior.behavior_data.get("credit_level"),
        "geo_risk": behavior.behavior_data.get("risk_zone"),
        "phone_prefix": profile.phone[:3],
    }
    return render(
        request,
        "recommendations.html",
        {
            "user": UserProfileSerializer(profile).data,
            "behavior": TransactionSerializer(behavior).data,
            "tags": recommendation_tags,
        },
    )


@require_http_methods(["POST"])
def third_party_send(request: HttpRequest) -> JsonResponse:
    user_id = int(request.POST.get("user_id", "0") or 0)
    endpoint = request.POST.get("endpoint", "https://ads.example.com/manual")
    triggered_by = request.POST.get("triggered_by", "manual_operator")
    result = send_payload_to_third_party(user_id=user_id, endpoint=endpoint, triggered_by=triggered_by)
    return JsonResponse(result)


@require_http_methods(["GET"])
def audit(request: HttpRequest) -> HttpResponse:
    rows = ThirdPartySync.objects.select_related("user").all().order_by("-id")
    return render(request, "audit.html", {"rows": ThirdPartySyncSerializer(rows, many=True).data})

def profile_page(request: HttpRequest) -> HttpResponse:
    user_id = request.GET.get("user_id")
    profile = UserProfile.objects.filter(user_id=user_id).first()
    behavior = BehaviorProfile.objects.filter(user_id=user_id).first()
    payload_preview = build_sync_payload(int(user_id or 0)) if user_id else {}
    return render(
        request,
        "profile.html",
        {
            "profile": UserProfileSerializer(profile).data if profile else {},
            "behavior": TransactionSerializer(behavior).data if behavior else {},
            "payload_preview": payload_preview,
        },
    )


def sync_page(request: HttpRequest) -> HttpResponse:
    return render(request, "sync.html")
