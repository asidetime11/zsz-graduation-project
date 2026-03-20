from django.contrib import admin

from .models import Appointment, PatientProfile

admin.site.register(PatientProfile)
admin.site.register(Appointment)
