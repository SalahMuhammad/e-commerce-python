from django.forms import ModelForm
from .models import Models, Items
from django import forms


class ModelForm(ModelForm):

    def clean_name(self):
        name_value = self.cleaned_data.get('name')

        if name_value:
            return name_value.lower().strip()

        return name_value

    class Meta:
        model = Models
        exclude = ['images']


class ItemForm(ModelForm):
    # just for testing
    comment = forms.CharField(max_length=20, widget=forms.Textarea)

    class Meta:
        model = Items
        # exclude = ['ram_type', 'hdd_type',
        #            'screen_resolution', 'gpu', 'sound_type']
        exclude = []
