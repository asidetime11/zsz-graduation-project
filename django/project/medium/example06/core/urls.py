from django.urls import path

from .views import survey_page, survey_results, survey_submit, user_profile

urlpatterns = [
    path("", survey_page, name="survey_home"),
    path("survey/submit/", survey_submit, name="survey_submit"),
    path("survey/results/", survey_results, name="survey_results"),
    path("users/profile/", user_profile, name="user_profile"),
]
