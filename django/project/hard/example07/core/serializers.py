from django.forms.models import model_to_dict

from .models import AuditLog, Transaction


class AuditLogSerializer:
    class Meta:
        model = AuditLog
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
        model = Transaction
        fields = "__all__"

    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(obj) for obj in self.instance]
        return model_to_dict(self.instance)
