from django.forms import (
    ModelForm,
    TextInput,
)

from .models import TspServiceDetails


class CrlUrlModify(ModelForm):
    class Meta:
        model = TspServiceDetails
        fields = ["crl_url"]
        labels = {"crl_url": False}
        widgets = {"crl_url": TextInput(attrs={"class": "form-control", "placeholder": " Enter correct CRL URL address"})}
