from items.models import *
from .serializers import *
from django.db.models import Q
from backend.utility import proccessStrParams
# 
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
import excelHandler


class TypesView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeeSerializer  


class ManufacturersView(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    

class ModelsView(viewsets.ModelViewSet):
    queryset = Models.objects.all()
    serializer_class = ModelSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        model = self.request.query_params.get('model')
        if model:
            queryset = queryset.filter(name__icontains=model)
        return queryset
    
 
class CPUGenerationsView(viewsets.ModelViewSet):
    queryset = CPUGeneration.objects.all()
    serializer_class = CPUGenerationsSerializer


class RamsView(viewsets.ModelViewSet):
    queryset = Ram.objects.all()
    serializer_class = RamsSerializer


class HDDSView(viewsets.ModelViewSet):
    queryset = HDD.objects.all()
    serializer_class = HDDsSerializer


class GPUsView(viewsets.ModelViewSet):
    queryset = GPU.objects.all()
    serializer_class = GPUsSerializer


class ScreenResolutionView(viewsets.ModelViewSet):
    queryset = ScreenResolution.objects.all()
    serializer_class = ScreenResolutionSerializer


class SoundTypesView(viewsets.ModelViewSet):
    queryset = SoundType.objects.all()
    serializer_class = SoundTypesSerializer


class ItemsView(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.query_params
        model_name = q.get('model-name')
        model_manufacturer = q.get('model-manufacturer')

        a = Q(model__name__icontains=model_name) if model_name is not None else Q(model__id__isnull=False)

        if model_name:
            queryset = queryset.filter(a)
        return queryset
    