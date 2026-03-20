from django.forms.models import model_to_dict

from .models import BehaviorProfile, ThirdPartySync, UserProfile


class UserProfileSerializer:
    class Meta:
        model = UserProfile
        fields = "__all__"

    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(obj) for obj in self.instance]
        return model_to_dict(self.instance)


class TransactionSerializer:
    class Meta:
        model = BehaviorProfile
        fields = "__all__"


class ThirdPartySyncSerializer:
    class Meta:
        model = ThirdPartySync
        fields = "__all__"

    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(obj) for obj in self.instance]
        return model_to_dict(self.instance)

    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(obj) for obj in self.instance]
        return model_to_dict(self.instance)
