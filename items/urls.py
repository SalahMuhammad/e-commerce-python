from django.urls import path
from .views import *

urlpatterns = [
    # path('', ImageView, name='img')
    path('', items, name='items'),
    path('item/<str:id>', item, name='item'),

    path('add-model/', Model.as_view(), name='add-model'),
    path('add-cpu/', cpuForm, name='add-cpu'),
    path('add-specifications/', specificationsForm, name='add-specifications'),
    path('add-item/', itemForm, name='add-item'),
]
