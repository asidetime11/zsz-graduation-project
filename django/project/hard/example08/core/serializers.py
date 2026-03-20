from django.forms.models import model_to_dict

from .models import UserProfile


class UserProfileSerializer:
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "org",
            "username",
            "email",
            "phone",
            "id_card",
            "ssn",
            "bank_account",
            "password_hash",
            "failed_login_count",
            "last_login",
            "internal_flags",
        ]

    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(obj) for obj in self.instance]
        return model_to_dict(self.instance)


class UserExportSerializer(UserProfileSerializer):
    pass
