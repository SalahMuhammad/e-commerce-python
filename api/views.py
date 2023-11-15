from items.models import Type, Manufacturer, Items
from .serializers import *
from django.db.models import Q
# 
from rest_framework import generics, viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from api.utilities import requestHandler

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


class ItemList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        edited_request = requestHandler(request=request)
        return self.create(edited_request, *args, **kwargs)


class ItemDetial(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request,*args, **kwargs):
        edited_request = requestHandler(request=request)
        return self.update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListCreateView2(generics.ListCreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    def create(self, request, *args, **kwargs):
        requestHandler(request=request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ListCreateView(APIView):

    def get(self, request, format=None):
        instances = Items.objects.all()
        serializer = ItemsSerializer(instances, many=True)
        return Response(serializer.data)
        

    def post(self, request):
        # specificationsHandler(request=request)
        print(request.data)
        for i in request.data['s-values']:
            print()
        serializer = ItemsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDestroyView(APIView):

    def get_object(self, pk):
        try:
            return Items.objects.get(pk=pk)
        except Items.DoesNotExist as e:
            print(f"Exception in get_object: {e}")
            raise Http404
        
    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = ItemsSerializer(instance)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        requestHandler(request=request)

        instance = self.get_object(pk)
        serializer = ItemsSerializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def a(request):
    raise TypeError("You tried to pass in the %s method name as a "
                                "keyword argument to %s(). Don't do that.")