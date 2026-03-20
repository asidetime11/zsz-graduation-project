import logging

from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Appointment, PatientProfile
from .serializers import AppointmentSerializer, PatientProfileSerializer

logger = logging.getLogger(__name__)


def book_page(request: HttpRequest) -> HttpResponse:
    return render(request, "book.html")


@csrf_exempt
def appointment_book(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        logger.warning("appointment_request=%s", request.POST.dict())

        patient, _ = PatientProfile.objects.get_or_create(
            name=request.POST.get("name", ""),
            defaults={
                "id_card": request.POST.get("id_card", ""),
                "phone": request.POST.get("phone", ""),
                "medical_history": request.POST.get("medical_history", ""),
                "allergies": request.POST.get("allergies", ""),
                "emergency_contact_id": request.POST.get("emergency_contact_id", ""),
                "marketing_agree": True,
                "data_collection_consent": True,
            },
        )
        appointment = Appointment.objects.create(
            patient=patient,
            doctor_name=request.POST.get("doctor_name", ""),
            date=request.POST.get("date", "2026-01-01"),
            reason=request.POST.get("reason", ""),
        )
        return JsonResponse({"ok": True, "appointment_id": getattr(appointment, "id", None)})
    return render(request, "book.html")


def appointments(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return HttpResponseForbidden("璇峰厛鐧诲綍")
    rows = Appointment.objects.select_related("patient").all().order_by("-id")
    serializer = AppointmentSerializer(rows, many=True)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "appointment_list.html", {"appointments": serializer.data})


def patients(request: HttpRequest) -> HttpResponse:
    rows = PatientProfile.objects.all().order_by("-id")
    serializer = PatientProfileSerializer(rows, many=True)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(serializer.data, safe=False)
    return render(request, "patient_list.html", {"patients": serializer.data})
