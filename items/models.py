from django.db import models


class CommonTypes(models.Model):
    type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type
    
    class Meta:
        abstract = True


class CommonBetweenHDDAndRam(models.Model):
    type = models.CharField(max_length=20)
    size = models.SmallIntegerField()

    def __str__(self):
        return str(self.size) + 'GB/' + self.type


    class Meta:
        abstract = True


class Type(CommonTypes):
    pass


class Manufacturer(CommonTypes):
    pass


class Models(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='models')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name='models')
    name = models.CharField(unique=True, max_length=50)
    images = models.ManyToManyField('ModelImages', related_name='models', blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.manufacturer.type + ' ' + self.name

    class Meta:
        ordering = ['manufacturer', 'name']


class ModelImages(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image.url

    def delete(self, *args, **kwargs):
        if self.image:
            storage, path = self.image.storage, self.image.path
            storage.delete(path)

        super().delete(*args, **kwargs)


class CPU(CommonTypes):
    pass


class CPUGeneration(models.Model):
    generation = models.CharField(max_length=30)
    cpu = models.ForeignKey(CPU, on_delete=models.PROTECT)

    def __str__(self):
        return self.cpu.type + '-' + self.generation


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['generation', 'cpu'],
                name='unique together cpu gen'
            )
        ]


class Ram(CommonBetweenHDDAndRam):

    
    class Meta:
        constraints = [
                models.UniqueConstraint(
                    fields=['type', 'size'],
                    name='unique together ram'
                )
            ]


class HDD(CommonBetweenHDDAndRam):


    class Meta:
        constraints = [
                models.UniqueConstraint(
                    fields=['type', 'size'],
                    name='unique together hdd'
                )
            ]


class GPU(CommonTypes):
    pass


class ScreenResolution(CommonTypes):
    pass


class SoundType(CommonTypes): 
    pass


class Items(models.Model):s
    model = models.ForeignKey(
        Models, related_name='items', on_delete=models.PROTECT)
    cpu = models.ForeignKey(CPUGeneration, 
                            null=True, 
                            blank=True, 
                            on_delete=models.PROTECT)
    ram = models.ManyToManyField(Ram, related_name='itemss')
    hdd = models.ManyToManyField(HDD, related_name='itemss')
    gpu = models.ManyToManyField(GPU, related_name='itemss')
    touch_screen = models.BooleanField(null=True, blank=True)  # verbose_name='touch'
    rotation = models.CharField(max_length=3, blank=True, null=True)
    illuminated_keyboard = models.BooleanField(null=True, blank=True, )
    original_windows = models.BooleanField(null=True, blank=True)
    screen_resolution = models.ForeignKey(ScreenResolution, on_delete=models.PROTECT, related_name='itemss')
    screen_size = models.FloatField(blank=True, null=True)
    sound_type = models.ForeignKey(SoundType, on_delete=models.PROTECT, related_name='itemss')
    price = models.IntegerField(null=True, blank=True)
    disc = models.SmallIntegerField(blank=True, null=True)
    note = models.CharField(max_length=50, null=True, blank=True)
    is_available = models.BooleanField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

        constraints = [
            models.UniqueConstraint(
                fields=['model', 'cpu', 'touch_screen', 'rotation', 'illuminated_keyboard', 
                        'original_windows', 'screen_resolution', 'screen_size', 'sound_type'],
                name='unique together'
            )
        ]
