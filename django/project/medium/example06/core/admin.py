from django.contrib import admin

from .models import Survey, SurveyResponse, UserProfile

admin.site.register(UserProfile)
admin.site.register(Survey)
admin.site.register(SurveyResponse)
