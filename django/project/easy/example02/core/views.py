from django.shortcuts import redirect, render
from .models import CandidateProfile


def submit_resume(request):
    if request.method == "POST":
        CandidateProfile.objects.create(
            name=request.POST.get("name", ""),
            email=request.POST.get("email", ""),
            id_card=request.POST.get("id_card", ""),
            phone=request.POST.get("phone", ""),
            marital_status=request.POST.get("marital_status", ""),
            religion=request.POST.get("religion", ""),
            medical_history=request.POST.get("medical_history", ""),
        )
        return redirect("resume_list")
    return render(request, "submit.html")


def resume_list(request):
    resumes = CandidateProfile.objects.all().order_by("-id")
    return render(request, "resume_list.html", {"resumes": resumes})
