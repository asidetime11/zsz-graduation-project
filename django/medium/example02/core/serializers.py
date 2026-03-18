from django.forms.models import model_to_dict

from .models import PaymentInfo


class PaymentInfoSerializer:
    class Meta:
        model = PaymentInfo
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.queryset]
        return model_to_dict(self.queryset)
