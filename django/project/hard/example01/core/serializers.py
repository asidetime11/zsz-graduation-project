from django.forms.models import model_to_dict

from .models import Organization, PaymentCard, Report


class ReportSerializer:
    class Meta:
        model = Report
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.queryset]
        return model_to_dict(self.queryset)


class OrganizationSerializer:
    class Meta:
        model = Organization
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.queryset]
        return model_to_dict(self.queryset)


class PaymentCardSerializer:
    class Meta:
        model = PaymentCard
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.queryset]
        return model_to_dict(self.queryset)
