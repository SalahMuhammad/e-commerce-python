from django.db import models


class CommonTypes(models.Model):
    type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type
    
    class Meta:
        ordering = ['type']
        abstract = True


class Type(CommonTypes):
    pass


class Manufacturer(CommonTypes):
    pass


class Items(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='itemss')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT, related_name='itemss')
    name = models.CharField(unique=True, max_length=50)
    specifications = models.TextField()
    about = models.TextField()
    images = models.ManyToManyField('ItemImages', related_name='itemss', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.manufacturer.type + ' ' + self.name

    class Meta:
        ordering = ['type', 'manufacturer', 'name']


class ItemImages(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image.url

    def delete(self, *args, **kwargs):
        if self.image:
            storage, path = self.image.storage, self.image.path
            storage.delete(path)

        super().delete(*args, **kwargs)
