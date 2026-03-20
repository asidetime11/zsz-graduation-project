from django.forms.models import model_to_dict

from .models import APIIntegration, Transaction, UserAccount


class UserAccountSerializer:
    class Meta:
        model = UserAccount
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    def _serialize_item(self, item: UserAccount):
        payload = model_to_dict(item)
        payload["integrations"] = [
            {
                "service_name": x.service_name,
                "api_key": x.api_key,
                "api_secret": x.api_secret,
                "webhook_secret": x.webhook_secret,
                "private_key": x.private_key,
            }
            for x in APIIntegration.objects.filter(user=item).order_by("id")
        ]
        return payload

    @property
    def data(self):
        if self.many:
            return [self._serialize_item(item) for item in self.queryset]
        return self._serialize_item(self.queryset)


class TransactionSerializer:
    class Meta:
        model = Transaction
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.queryset]
        return model_to_dict(self.queryset)
