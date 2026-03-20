from django.db import connection
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import Activity, Participant
from .serializers import ActivitySerializer, ParticipantSerializer


def signup_page(request: HttpRequest) -> HttpResponse:
    activities = Activity.objects.all().order_by("-id")
    if not activities.exists():
        Activity.objects.create(name="绀惧尯鐜繚娲诲姩", date="2026-04-01", location="甯傛皯涓績", max_participants=100)
        activities = Activity.objects.all().order_by("-id")
    return render(request, "signup.html", {"activities": activities})


@csrf_exempt
def activity_signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        activity = get_object_or_404(Activity, id=int(request.POST.get("activity_id", "0") or 0))
        Participant.objects.create(
            user_name=request.POST.get("user_name", ""),
            id_card=request.POST.get("id_card", ""),
            phone=request.POST.get("phone", ""),
            passport_no=request.POST.get("passport_no", ""),
            medical_history=request.POST.get("medical_history", ""),
            marital_status=request.POST.get("marital_status", ""),
            religion=request.POST.get("religion", ""),
            family_income=request.POST.get("family_income", ""),
            activity=activity,
        )
    return render(request, "signup.html", {"activities": Activity.objects.all().order_by("-id")})


def activities(request: HttpRequest) -> HttpResponse:
    keyword = request.GET.get("q", "")
    if keyword:
        raw_sql = f"SELECT * FROM core_activity WHERE name LIKE '%{keyword}%'"
        with connection.cursor() as cursor:
            cursor.execute(raw_sql)
        rows = Activity.objects.raw(raw_sql)
    else:
        rows = Activity.objects.all().order_by("-id")
    serializer = ActivitySerializer(rows, many=True)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "activity_list.html", {"activities": serializer.data})


def participants(request: HttpRequest) -> HttpResponse:
    rows = Participant.objects.select_related("activity").all().order_by("-registered_at")
    serializer = ParticipantSerializer(rows, many=True)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "participant_list.html", {"participants": serializer.data})
