from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'types', views.TypesView)
router.register(r'manufacturers', views.ManufacturersView)
router.register(r'models', views.ModelsView)
router.register(r'cpus', views.CPUGenerationsView)
router.register(r'rams', views.RamsView)
router.register(r'hdds', views.HDDSView)
router.register(r'screen-resolution', views.ScreenResolutionView)
router.register(r'sound-types', views.SoundTypesView)
router.register(r'items', views.ItemsView)

urlpatterns = [
    path(r'', include(router.urls))
]
