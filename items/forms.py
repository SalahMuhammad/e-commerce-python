from django.forms import ModelForm
from .models import Model


class ModelForm(ModelForm):
    class Meta:
        model = Model
        fields = '__all__'
