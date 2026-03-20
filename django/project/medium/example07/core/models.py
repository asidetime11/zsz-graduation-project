from django.db import models


class PatientProfile(models.Model):
    name = models.CharField(max_length=100)
    id_card = models.CharField(max_length=32)
    phone = models.CharField(max_length=20)
    medical_history = models.TextField()
    allergies = models.TextField(blank=True)
    emergency_contact_id = models.CharField(max_length=64)
    marketing_agree = models.BooleanField(default=True)
    data_collection_consent = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="appointments")
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name}-{self.doctor_name}-{self.date}"
