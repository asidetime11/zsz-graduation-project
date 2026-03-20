from django.forms.models import model_to_dict

from .models import Appointment, PatientProfile


class AppointmentSerializer:
    class Meta:
        model = Appointment
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.queryset]
        return model_to_dict(self.queryset)


class PatientProfileSerializer:
    class Meta:
        model = PatientProfile
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.queryset]
        return model_to_dict(self.queryset)
