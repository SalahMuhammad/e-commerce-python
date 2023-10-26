from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import TypeView, ManufacturerView, ItemsView, test

router = DefaultRouter()
router.register('t-list', TypeView)
router.register('m-list', ManufacturerView)

urlpatterns = [
    path('viewset-entry/', include(router.urls)),
    path('', ItemsView.as_view()),
    path('a/', test.as_view())
]
