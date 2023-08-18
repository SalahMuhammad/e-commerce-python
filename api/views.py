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
        type_list, cpu_list, cpu_type_list, ram_list, hdd_list = proccessStrParams(
            self.kwargs['typee'],
            self.kwargs['cpu'],
            self.kwargs['cpu_type'],
            self.kwargs['ram'],
            self.kwargs['hdd']
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

        is_available = Q(is_available=True)

        queryset = Item.objects.filter(
            type_list & cpu_list & cpu_type_list & ram_list & hdd_list & is_available)

        return queryset


@api_view(['GET'])
def cpuTypes(req, id):
    listt, = proccessStrParams(id)

    availableCPUGenerations = Item.objects.filter(Q(is_available=True) &
                                                  Q(cpu_type__name__id__in=listt)).values_list('cpu_type')

    qObject = Q(id__in=[i[0] for i in availableCPUGenerations])

    cpuTypes = CPUType.objects.filter(qObject)

    serializer = CPUTypeSerializer(cpuTypes, many=True)

    return Response(serializer.data)
