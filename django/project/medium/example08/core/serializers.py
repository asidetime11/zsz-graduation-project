from django.forms.models import model_to_dict

from .models import Activity, Participant


class ParticipantSerializer:
    class Meta:
        model = Participant
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.queryset]
        return model_to_dict(self.queryset)


class ActivitySerializer:
    class Meta:
        model = Activity
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.queryset]
        return model_to_dict(self.queryset)
