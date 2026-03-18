from django.forms.models import model_to_dict

from .models import Order, User


class UserSerializer:
    class Meta:
        model = User
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(obj) for obj in self.queryset]
        return model_to_dict(self.queryset)


class OrderSerializer:
    class Meta:
        model = Order
        fields = "__all__"

    def __init__(self, queryset, many=False):
        self.queryset = queryset
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(obj) for obj in self.queryset]
        return model_to_dict(self.queryset)
