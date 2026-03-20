from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import UserActivity, UserProfile
from .serializers import UserActivitySerializer


def seed_demo_data() -> None:
    if not UserProfile.objects.exists():
        alice = UserProfile.objects.create(
            username="alice",
            email="alice@example.com",
            phone="13800001111",
            id_card="110101199901011111",
        )
        bob = UserProfile.objects.create(
            username="bob",
            email="bob@example.com",
            phone="13900002222",
            id_card="110101199202022222",
        )
        UserActivity.objects.create(
            user=alice,
            action="login",
            ip_address="127.0.0.1",
            user_agent="Mozilla/5.0 seed-agent",
            session_id="seed-a1",
        )
        UserActivity.objects.create(
            user=bob,
            action="view_stats",
            ip_address="10.1.1.15",
            user_agent="Mozilla/5.0 seed-agent-2",
            session_id="seed-b2",
        )


@csrf_exempt
def track(request: HttpRequest) -> HttpResponse:
    seed_demo_data()
    if request.method == "POST":
        user_id = int(request.POST.get("user_id", "1") or 1)
        action = request.POST.get("action", "visit")
        session_id = request.POST.get("session_id", "")

        user = get_object_or_404(UserProfile, id=user_id)
        UserActivity.objects.create(
            user=user,
            action=action,
            ip_address=request.META.get("REMOTE_ADDR", "127.0.0.1"),
            user_agent=request.META.get("HTTP_USER_AGENT", "unknown-agent"),
            session_id=session_id,
        )
        return JsonResponse({"ok": True})

    users = UserProfile.objects.all().order_by("id")
    return render(request, "stats.html", {"users": users})


def activities(request: HttpRequest) -> HttpResponse:
    seed_demo_data()
    action_kw = request.GET.get("action", "")
    records = UserActivity.objects.select_related("user").all().order_by("-timestamp")
    if action_kw:
        records = records.filter(action__icontains=action_kw)

    serializer = UserActivitySerializer(records, many=True)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "activity_list.html", {"activities": serializer.data})


@csrf_exempt
def delete_user(request: HttpRequest, user_id_path: int) -> HttpResponse:
    seed_demo_data()
    user = get_object_or_404(UserProfile, id=user_id_path)
    if request.method == "DELETE" or request.POST.get("_method") == "DELETE":
        user.delete()
        return JsonResponse({"ok": True, "message": "user deleted but activities preserved"})
    return JsonResponse({"ok": False, "message": "method not allowed"}, status=405)


def user_manage(request: HttpRequest) -> HttpResponse:
    seed_demo_data()
    users = UserProfile.objects.all().order_by("-created_at")
    return render(request, "user_manage.html", {"users": users})


def stats(request: HttpRequest) -> HttpResponse:
    seed_demo_data()
    total_users = UserProfile.objects.count()
    total_activities = UserActivity.objects.count()
    return render(request, "stats.html", {"total_users": total_users, "total_activities": total_activities, "users": UserProfile.objects.all().order_by("id")})
