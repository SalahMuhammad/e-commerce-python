from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import TypeView, ManufacturerView, ItemsView, ListCreateView, RetrieveUpdateDestroyView, ListCreateView2, ItemList

router = DefaultRouter()
router.register('t-list', TypeView)
router.register('m-list', ManufacturerView)

urlpatterns = [
    path('viewset-entry/', include(router.urls)),
    path('', ItemsView.as_view()),
    path('a/', ListCreateView.as_view()),
    path('b/', ListCreateView2.as_view()),
    path('a/<int:pk>/', RetrieveUpdateDestroyView.as_view()),
    path('c/', ItemList.as_view()),
    path('c/<int:pk>/', RetrieveUpdateDestroyView.as_view()),
]
