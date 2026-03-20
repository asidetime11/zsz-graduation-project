from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import Survey, SurveyResponse, UserProfile
from .serializers import SurveyResponseSerializer, UserProfileSerializer


def survey_page(request: HttpRequest) -> HttpResponse:
    surveys = Survey.objects.all().order_by("-id")
    if not surveys.exists():
        Survey.objects.create(title="鐢ㄦ埛婊℃剰搴﹁皟鏌?, description="鏀堕泦鐢ㄦ埛鏈嶅姟鍙嶉")
        surveys = Survey.objects.all().order_by("-id")
    return render(request, "survey.html", {"surveys": surveys})


@csrf_exempt
def survey_submit(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        id_card = request.POST.get("id_card", "")
        user_ip = request.META.get("REMOTE_ADDR", "127.0.0.1")
        survey_id = int(request.POST.get("survey_id", "0") or 0)

        user, _ = UserProfile.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "phone": phone,
                "id_card": id_card,
                "ip_address": user_ip,
            },
        )
        survey = get_object_or_404(Survey, id=survey_id)
        SurveyResponse.objects.create(
            user=user,
            survey=survey,
            answers=request.POST.get("answers", ""),
            family_income=request.POST.get("family_income", ""),
            ip_address=user_ip,
        )
    return render(request, "survey.html", {"surveys": Survey.objects.all().order_by("-id")})


def survey_results(request: HttpRequest) -> HttpResponse:
    responses = SurveyResponse.objects.select_related("user", "survey").all().order_by("-submitted_at")
    serializer = SurveyResponseSerializer(responses, many=True)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "results.html", {"responses": serializer.data})


def user_profile(request: HttpRequest) -> HttpResponse:
    users = UserProfile.objects.all().order_by("-id")
    serializer = UserProfileSerializer(users, many=True)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "profile.html", {"users": serializer.data})
