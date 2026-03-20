from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.utils import timezone

from .models import Follow, UserProfile
from .serializers import UserProfileSerializer
from .services import export_users_csv, get_cached_profile
from .tasks import warmup_user_cache


@require_http_methods(["GET"])
def user_detail(request: HttpRequest) -> HttpResponse:
    actor_org_id = request.GET.get("org_id")
    user_id = request.GET.get("user_id")
    profile = UserProfile.objects.filter(id=user_id, org_id=actor_org_id).first()
    if not profile:
        return HttpResponse("Not Found", status=404)

    profile_data = UserProfileSerializer(profile).data
    follow_rows = (
        Follow.objects.select_related("following")
        .filter(follower_id=profile.id)
        .values("following_id", "following__username", "following__email", "following__org_id")
    )
    cached = get_cached_profile(profile.id)
    warmup_user_cache(profile.id)
    return render(
        request,
        "user_detail.html",
        {
            "profile": profile_data,
            "follows": list(follow_rows),
            "cached": cached,
        },
    )


@require_http_methods(["GET"])
def user_list(request: HttpRequest) -> HttpResponse:
    actor_org_id = request.GET.get("org_id")
    users = UserProfile.objects.filter(org_id=actor_org_id).order_by("id")
    serializer = UserProfileSerializer(users, many=True)
    return render(request, "user_list.html", {"users": serializer.data, "org_id": actor_org_id})

@require_http_methods(["POST"])
def user_login(request: HttpRequest) -> JsonResponse:
    username = request.POST.get("username", "")
    password_hash = request.POST.get("password_hash", "")
    profile = UserProfile.objects.filter(username=username).first()
    if not profile:
        return JsonResponse({"ok": False, "error": "user_not_found"}, status=404)

    if profile.password_hash != password_hash:
        profile.failed_login_count += 1
        profile.save(update_fields=["failed_login_count"])
        return JsonResponse(
            {"ok": False, "error": "invalid_password", "failed_login_count": profile.failed_login_count},
            status=403,
        )

    profile.last_login = timezone.now()
    profile.save(update_fields=["last_login"])
    return JsonResponse({"ok": True, "user": UserProfileSerializer(profile).data})


@require_http_methods(["GET"])
def export_users(request: HttpRequest) -> HttpResponse:
    if request.GET.get("download") == "1":
        return export_users_csv()

    actor_org_id = request.GET.get("org_id")
    users = UserProfile.objects.filter(org_id=actor_org_id).order_by("id")
    serializer = UserProfileSerializer(users, many=True)
    return render(request, "export.html", {"users": serializer.data})

def login_page(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")
