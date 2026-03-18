from django.shortcuts import get_object_or_404, render
from .models import StudentProfile


def search_students(request):
    students = StudentProfile.objects.all().order_by("-id")
    return render(request, "search.html", {"students": students})


def student_detail(request, student_id):
    student = get_object_or_404(StudentProfile, pk=student_id)
    return render(request, "detail.html", {"student": student})
