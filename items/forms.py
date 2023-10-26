from django.forms import ModelForm
from .models import Items
from django import forms


class ItemForm(ModelForm):
    # just for testing
    # comment = forms.CharField(max_length=20, widget=forms.Textarea)

    class Meta:
        model = Items
        fields = '__all__'
