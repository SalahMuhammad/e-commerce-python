from django.forms import ModelForm
from .models import Model, Manufacturer, Type, Item, CPUType


class ModelForm(ModelForm):

    def clean_name(self):
        name_value = self.cleaned_data.get('name')

        if name_value:
            return name_value.lower()

        return name_value

    class Meta:
        model = Model
        fields = ['name', 'note']


class ManufacturerForm(ModelForm):

    class Meta:
        model = Manufacturer
        fields = '__all__'


class ItemForm(ModelForm):

    class Meta:
        model = Item
        exclude = ['ram_type', 'hdd_type',
                   'screen_resolution', 'gpu', 'sound_type']


class CPUTypeForm(ModelForm):

    class Meta:
        model = CPUType
        fields = ['cpu_type']
