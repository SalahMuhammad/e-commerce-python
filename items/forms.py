from django.forms import ModelForm
from .models import Model, Manufacturer, Type, Item


class ModelForm(ModelForm):
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
