from django.contrib import admin
from .models import *


# class ItemsAdmin(admin.ModelAdmin):
#     # list_display = 'labtop',
#     list_display = (
#         'manufacturer',
#         'model',
#         'cpu',
#         'cpu_speed',
#         'ram',
#         'hdd',
#         'screen_size',
#         'gpu',
#         'touch_screen',
#         'rotation',
#         'illuminated_keyboard',
#         'original_windows',
#         'screen_resolution',
#         'sound_type',
#         # 'note',
#         'count'
#     )

# class ManufacturerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')


# class TypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')


# class ModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'manufacturer', 'typee', 'cpu_type', 'ram_type')


# admin.site.register(Models)
admin.site.register(Items)
