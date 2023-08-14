from django.urls import path, re_path
from .views import *


urlpatterns = [
    # path('', ImageView, name='img')
    path('', items, name='items'),
    path('item/<str:id>', item, name='item'),


    path('models/', Models.as_view(), name='model-list'),
    path('models/create', ModelCreate.as_view(), name='create-model'),
    re_path(r'^models/update/(?P<pk>\d{0,4})/$',
            ModelUpdate.as_view(), name='update-model'),


    # path('add-model/', Model.as_view(), name='add-model'),
    path('create-cpu/', cpuForm, name='create-cpu'),


    path('items/', Items.as_view(), name='item-list'),
    path('items/create/', ItemCreate.as_view(), name='create-item'),
    re_path(r'^items/update/(?P<pk>\d{0,4})/$',
            ItemUpdate.as_view(), name='update-item')
]
