from rest_framework import serializers
from items.models import *


class TypeeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Type
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Manufacturer
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Models
        fields = '__all__'


class CPUGenerationsSerializer(serializers.ModelSerializer):
    cpu = serializers.SerializerMethodField()

    def get_cpu(self, obj):
        return obj.cpu.type + '-' + obj.generation


    class Meta:
        model = CPUGeneration
        fields = ['id', 'cpu']


class RamsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ram
        fields = '__all__'


class HDDsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HDD
        fields = '__all__'


class GPUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GPU
        fields = '__all__'


class ScreenResolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScreenResolution
        fields = '__all__'


class SoundTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoundType
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    ggg = serializers.SerializerMethodField()

    def get_ggg(self, obj):
        return obj.model.manufacturer.type + '-' + obj.model.name
    

    class Meta:
        model = Items
        # exclude = ['price', 'disc', 'screen_size', 'illuminated_keyboard',
        #            'original_windows', 'rotation', 'touch_screen', 'created', 'updated', 'is_available']
        fields = '__all__'
        # depth = 2
