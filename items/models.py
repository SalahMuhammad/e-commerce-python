import os
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class Model(models.Model):
    typee = models.ForeignKey(Type, on_delete=models.PROTECT)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    name = models.CharField(unique=True, max_length=50)
    # specifications = models.ManyToManyField(
    #     'Specifications', related_name='sp')
    note = models.CharField(max_length=500, blank=True)
    images = models.ManyToManyField('Image', related_name='im')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  # self.manufacturer.name + ' ' + self.name

    class Meta:
        ordering = ['manufacturer__name', 'name']


# def get_upload_path(instance, filename):
#     return os.path.join(
#         "user_%d" % instance.manufacturer.id, "car_%s" % instance.name, filename)


# def user_directory_path(instance, filename, fdsa):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return "user_{0}/{1}".format(instance.image.id, filename)


class Image(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image.url

    def delete(self, *args, **kwargs):
        if self.image:
            storage, path = self.image.storage, self.image.path
            storage.delete(path)

        super().delete(*args, **kwargs)


# class Specifications(models.Model):
#     touch_screen = models.BooleanField()
#     rotation = models.CharField(max_length=3)
#     illuminated_keyboard = models.BooleanField()
#     original_windows = models.BooleanField()
#     screen_resolution = models.ForeignKey(
#         'ScreenResolution', on_delete=models.PROTECT, related_name='sr')
#     screen_size = models.FloatField()
#     sound_type = models.ForeignKey('SoundType', on_delete=models.PROTECT)

#     class Meta:
#         unique_together = ["touch_screen", "rotation", "illuminated_keyboard",
#                            'original_windows', 'screen_resolution', 'screen_size', 'sound_type']

#     # def __str__(self):
#         # return str(True) if self.touch_screen == True else str(False) + ' ' + self.rotation + ' ' + str(True) if self.illuminated_keyboard == True else str(False) + ' ' + str(True) if self.original_windows == True else str(False) + ' ' + self.screen_resolution + ' ' + self.sound_type.name


class CPU(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class CPUType(models.Model):
    name = models.ForeignKey(CPU, on_delete=models.PROTECT)
    cpu_type = models.CharField(max_length=30)

    def __str__(self):
        # self.name.name + ' ' + self.cpu_type
        return self.name.name + '-' + self.cpu_type

    class Meta:
        ordering = ['cpu_type']


class GPUType(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class RamType(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class HDDType(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class ScreenResolution(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class SoundType(models.Model):
    name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.name


class Item(models.Model):
    model = models.ForeignKey(
        Model, related_name='items', on_delete=models.PROTECT)
    cpu_type = models.ForeignKey('CPUType', on_delete=models.PROTECT)
    cpu_speed = models.FloatField(blank=True, null=True)
    ram_type = models.ForeignKey('RamType', on_delete=models.PROTECT)
    ram_cache = models.SmallIntegerField(verbose_name='ram speed')
    hdd_type = models.ForeignKey('HDDType', on_delete=models.PROTECT)
    hdd_size = models.SmallIntegerField()
    gpu = models.ForeignKey('GPUType', on_delete=models.PROTECT)
    touch_screen = models.BooleanField(verbose_name='touch')
    rotation = models.CharField(max_length=3, blank=True, null=True)
    illuminated_keyboard = models.BooleanField()
    original_windows = models.BooleanField()
    screen_resolution = models.ForeignKey(
        'ScreenResolution', on_delete=models.PROTECT, verbose_name='resolution')
    screen_size = models.FloatField(blank=True, null=True)
    sound_type = models.ForeignKey('SoundType', on_delete=models.PROTECT)
    price = models.IntegerField()
    disc = models.SmallIntegerField('discount', blank=True, null=True)
    is_available = models.BooleanField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

        constraints = [
            models.UniqueConstraint(
                fields=['model', 'cpu_type', 'cpu_speed', 'ram_type', 'ram_cache', 'hdd_type', 'hdd_size', 'gpu',
                        'touch_screen', 'rotation', 'illuminated_keyboard', 'original_windows', 'screen_resolution', 'screen_size', 'sound_type'],
                name='unique together'
            )
        ]
    # unique_together = ['model', 'cpu_type', 'cpu_speed', 'ram_type', 'ram_cache', 'hdd_type', 'hdd_size', 'gpu',
    #                            'touch_screen', 'rotation', 'illuminated_keyboard', 'original_windows','screen_resolution', 'screen_size', 'sound_type']
