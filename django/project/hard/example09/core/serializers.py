from django.forms.models import model_to_dict

from .models import Report, UserProfile


class UserProfileSerializer:
    class Meta:
        model = UserProfile
        fields = ["id", "username", "email", "id_card", "api_key", "org_id"]

    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(obj) for obj in self.instance]
        return model_to_dict(self.instance)


class ReportSerializer:
    class Meta:
        model = Report
        fields = "__all__"

    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(obj) for obj in self.instance]
        return model_to_dict(self.instance)
