from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from items.models import Item, CPUType
# , CPU, HDDType, Model, Image, Manufacturer
from datetime import datetime


class CPUTypeSerializer(ModelSerializer):

    class Meta:
        model = CPUType
        exclude = ['name']


class ItemSerializer(ModelSerializer):

    class Meta:
        model = Item
        exclude = ['price', 'disc', 'screen_size', 'illuminated_keyboard',
                   'original_windows', 'rotation', 'touch_screen', 'created', 'updated', 'is_available']
        depth = 2
