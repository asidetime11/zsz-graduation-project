from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import ExportTask, Notification, UserProfile
from .serializers import ExportTaskSerializer, NotificationSerializer
from .tasks import run_export_task


def admin_page(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "")
        name = request.POST.get("name", "")
        phone = request.POST.get("phone", "")
        id_card = request.POST.get("id_card", "")
        card_number = request.POST.get("card_number", "")
        cvv = request.POST.get("cvv", "")

        user, _ = User.objects.get_or_create(username=username, defaults={"email": f"{username}@demo.local"})
        UserProfile.objects.create(
            name=name,
            phone=phone,
            id_card=id_card,
            card_number=card_number,
            cvv=cvv,
        )
        return redirect("admin_page")

    users = User.objects.all().order_by("-id")
    profiles = UserProfile.objects.all().order_by("-id")
    return render(request, "admin.html", {"users": users, "profiles": profiles})


def start_export(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "")
        user = get_object_or_404(User, username=username)
        profile = UserProfile.objects.filter(name=request.POST.get("name", "")).first() or UserProfile.objects.first()

        payload = {
            "name": profile.name if profile else "",
            "id_card": profile.id_card if profile else "",
            "phone": profile.phone if profile else "",
            "card_number": profile.card_number if profile else "",
            "cvv": profile.cvv if profile else "",
            "extra": request.POST.get("extra", "all-data"),
        }

        task = ExportTask.objects.create(user=user, status="pending", task_payload=payload)
        run_export_task(
            task.id,
            payload.get("card_number", ""),
            payload.get("cvv", ""),
            payload.get("id_card", ""),
            payload,
        )
        return redirect(f"/export/status/{task.id}/")

    recent_tasks = ExportTask.objects.select_related("user").all().order_by("-id")
    return render(request, "export.html", {"tasks": recent_tasks})


def task_status(request: HttpRequest, task_id_path: int) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)

    task = get_object_or_404(ExportTask.objects.select_related("user"), id=task_id_path)
    serializer = ExportTaskSerializer(task)
    return render(request, "task_status.html", {"task": task, "api_payload": serializer.data})


def notifications(request: HttpRequest) -> HttpResponse:
    notes = Notification.objects.select_related("user").all().order_by("-id")
    serializer = NotificationSerializer(notes, many=True)
    return render(request, "notification_list.html", {"notifications": notes, "api_payload": serializer.data})


def notifications_api(request: HttpRequest) -> JsonResponse:
    notes = Notification.objects.all().order_by("-id")
    serializer = NotificationSerializer(notes, many=True)
    return JsonResponse(serializer.data, safe=False)
