from django.shortcuts import redirect, render
from .models import Feedback


def feedback(request):
    if request.method == "POST":
        Feedback.objects.create(
            name=request.POST.get("name", ""),
            email=request.POST.get("email", ""),
            phone=request.POST.get("phone", ""),
            feedback_content=request.POST.get("feedback_content", ""),
        )
        return redirect("feedback_list")
    return render(request, "feedback.html")


def feedback_list(request):
    items = Feedback.objects.all().order_by("-id")
    return render(request, "feedback_list.html", {"items": items})
