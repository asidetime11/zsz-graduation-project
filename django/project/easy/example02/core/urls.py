from django.urls import path
from .views import resume_list, submit_resume

urlpatterns = [
    path("resume/submit/", submit_resume, name="submit_resume"),
    path("resumes/", resume_list, name="resume_list"),
]
