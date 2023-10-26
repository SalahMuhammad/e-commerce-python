from rest_framework import serializers
from items.models import Type, Manufacturer, Items


class TypeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Type
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Manufacturer
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    # ggg = serializers.SerializerMethodField()

    # def get_ggg(self, obj):
    #     return obj.model.manufacturer.type + '-' + obj.model.name
    

    class Meta:
        model = Items
        fields = '__all__'
