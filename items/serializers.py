# from rest_framework import serializers
from .models import Items


# from datetime import datetime
# 
# class ItemsSerializers(serializers.ModelSerializer):
#     # url = serializers.CharField(source='get_absolute_url', read_only=True)
#     # groups = serializers.PrimaryKeyRelatedField(many=True)

#     class Meta:
#         model = Items
#         # for item in a:
#         #     Items.save(Items(
#         #             manufacturer=item['manufacturer'],
#         #             model=item['model'],
#         #             cpu=item['cpu'],
#         #             cpu_speed=item['cpu_speed'],
#         #             ram=item['ram'],
#         #             hdd=item['hdd'],
#         #             screen_size=item['screen_size'],
#         #             gpu=item['gpu'],
#         #             touch_screen=item['touch_screen'],
#         #             rotation=item['rotation_360deg'],
#         #             illuminated_keyboard=item['illuminated_keyboard'],
#         #             original_windows=item['original_windows'],
#         #             screen_resolution=item['screen_resolution'],
#         #             sound_type=item['sound_type'],
#         #             count=item['count']
#         #         )
#         #     )
#         # print('done')
#         # i = Items(model=321)
#         # Items.save(i)
#         # fields = ('id', 'labtop')
#         fields = (
#             'id',
#             'manufacturer',
#             'model',
#             'cpu',
#             'cpu_speed',
#             'ram',
#             'hdd',
#             'screen_size',
#             'gpu',
#             'touch_screen',
#             'rotation',
#             'illuminated_keyboard',
#             'original_windows',
#             'screen_resolution',
#             'sound_type',
#             # 'note',
#             # 'count'
#         )


# class ItemsSerializers1(serializers.ModelSerializer):
#     # url = serializers.CharField(source='get_absolute_url', read_only=True)
#     # groups = serializers.PrimaryKeyRelatedField(many=True)

#     class Meta:
#         model = Items
#         # for item in a:
#         #     Items.save(Items(
#         #             manufacturer=item['manufacturer'],
#         #             model=item['model'],
#         #             cpu=item['cpu'],
#         #             cpu_speed=item['cpu_speed'],
#         #             ram=item['ram'],
#         #             hdd=item['hdd'],
#         #             screen_size=item['screen_size'],
#         #             gpu=item['gpu'],
#         #             touch_screen=item['touch_screen'],
#         #             rotation=item['rotation_360deg'],
#         #             illuminated_keyboard=item['illuminated_keyboard'],
#         #             original_windows=item['original_windows'],
#         #             screen_resolution=item['screen_resolution'],
#         #             sound_type=item['sound_type'],
#         #             count=item['count']
#         #         )
#         #     )
#         # print('done')
#         # i = Items(model=321)
#         # Items.save(i)
#         # fields = ('id', 'labtop')
#         fields = (
#             'id',
#             # 'manufacturer',
#             'model',
#             'cpu',
#             # 'cpu_speed',
#             'ram',
#             'hdd',
#             # 'screen_size',
#             'gpu',
#             # 'touch_screen',
#             # 'rotation',
#             # 'illuminated_keyboard',
#             # 'original_windows',
#             # 'screen_resolution',
#             # 'sound_type',
#             # 'note',
#             # 'count'
#         )