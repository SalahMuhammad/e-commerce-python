from items.models import Type, Manufacturer, Items
from .serializers import *
from django.db.models import Q
# 
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView


class TypeView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class ManufacturerView(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ItemsView(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    
    def post(self, request):
        request.data['about'] = 'hello world'
        print(request.data.get('about'))
        super().post(request)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


class test(APIView):
    def get(self, request, format=None):
        snippets = Items.objects.all()
        serializer = ItemsSerializer(snippets, many=True)
        return Response(serializer.data)
        

    def post(self, request):
        # about = request.data.get('about')
        # request.data['about'] = 'fdssssssss'
        # print(request.data.get('about'))
        # request.data['specifications'][0] = 'fdsfdas'
        print(request.data)
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def a(request):
    raise TypeError("You tried to pass in the %s method name as a "
                                "keyword argument to %s(). Don't do that.")