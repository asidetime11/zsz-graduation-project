from django.forms.models import model_to_dict

from .models import Document


class DocumentSerializer:
    class Meta:
        model = Document
        fields = "__all__"

    def __init__(self, instance, many=False):
        self.instance = instance
        self.many = many

    @property
    def data(self):
        if self.many:
            return [model_to_dict(item) for item in self.instance]
        return model_to_dict(self.instance)
