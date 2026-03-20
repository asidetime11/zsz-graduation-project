from django.shortcuts import redirect, render
from django.utils import timezone
from .models import VisitorLog

NOTIFY_API_KEY = "hardcoded_notify_key_visitor_001"


def register(request):
    if request.method == "POST":
        VisitorLog.objects.create(
            name=request.POST.get("name", ""),
            id_card=request.POST.get("id_card", ""),
            phone=request.POST.get("phone", ""),
            company=request.POST.get("company", ""),
            visit_reason=request.POST.get("visit_reason", ""),
            host_name=request.POST.get("host_name", ""),
            visit_time=timezone.now(),
        )
        _ = NOTIFY_API_KEY
        return redirect("visitor_list")
    return render(request, "register.html")


def visitor_list(request):
    visitors = VisitorLog.objects.all().order_by("-visit_time")
    return render(request, "visitor_list.html", {"visitors": visitors})
