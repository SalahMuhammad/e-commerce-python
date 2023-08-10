from items.models import Item, CPUType
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer, CPUTypeSerializer
from django.db.models import Q
from backend.utility import proccessStrParams

from rest_framework import generics


# @api_view(['GET'])
# def items(req, typee, cpu, cpu_type, ram, hdd, gpu):
#     type_list, cpu_list, cpu_type_list, ram_list, hdd_list, gpu_list = proccessStrParams(
#         typee,
#         cpu,
#         cpu_type,
#         ram,
#         hdd,
#         gpu
#     )

#     type_list = Q(model__typee__id__in=type_list) if type_list else Q(
#         model__typee__id__isnull=False)

#     cpu_list = Q(cpu_type__name__id__in=cpu_list) if cpu_list else Q(
#         cpu_type__name__id__isnull=False)

#     cpu_type_list = Q(cpu_type__id__in=cpu_type_list) if cpu_type_list else Q(
#         cpu_type__id__isnull=False)

#     ram_list = Q(ram_type__id__in=ram_list) if ram_list else Q(
#         ram_type__id__isnull=False)

#     hdd_list = Q(hdd_type__id__in=hdd_list) if hdd_list else Q(
#         cpu_type__id__isnull=False)

#     gpu_list = Q(gpu__id__in=gpu_list) if gpu_list else Q(
#         gpu__id__isnull=False)

#     items = Item.objects.filter(
#         type_list & cpu_list & cpu_type_list & ram_list & hdd_list & gpu_list)

#     serializer = ItemSerializer(items, many=True)

#     return Response(serializer.data)


class Items(generics.ListAPIView):
    # queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        type_list, cpu_list, cpu_type_list, ram_list, hdd_list, gpu_list = proccessStrParams(
            self.kwargs['typee'],
            self.kwargs['cpu'],
            self.kwargs['cpu_type'],
            self.kwargs['ram'],
            self.kwargs['hdd'],
            self.kwargs['gpu']
        )

        type_list = Q(model__typee__id__in=type_list) if type_list else Q(
            model__typee__id__isnull=False)

        cpu_list = Q(cpu_type__name__id__in=cpu_list) if cpu_list else Q(
            cpu_type__name__id__isnull=False)

        cpu_type_list = Q(cpu_type__id__in=cpu_type_list) if cpu_type_list else Q(
            cpu_type__id__isnull=False)

        ram_list = Q(ram_type__id__in=ram_list) if ram_list else Q(
            ram_type__id__isnull=False)

        hdd_list = Q(hdd_type__id__in=hdd_list) if hdd_list else Q(
            cpu_type__id__isnull=False)

        gpu_list = Q(gpu__id__in=gpu_list) if gpu_list else Q(
            gpu__id__isnull=False)

        queryset = Item.objects.filter(
            type_list & cpu_list & cpu_type_list & ram_list & hdd_list & gpu_list)

        return queryset


@api_view(['GET'])
def cpuTypes(req, id):
    list, = proccessStrParams(id)

    list = Q(name__id__in=list)

    cpuTypes = CPUType.objects.filter(list)

    serializer = CPUTypeSerializer(cpuTypes, many=True)

    return Response(serializer.data)
