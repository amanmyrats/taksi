from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

from PIL import Image

from .utils import user_photo_upload_path, car_photo_upload_path


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class TaxiProfile(models.Model):    
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    mobile=models.CharField(max_length=13)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True,  blank=True)
    status = models.ForeignKey(Status, on_delete = models.SET_NULL, null = True,  blank=True)
    nireden = models.ForeignKey(City, on_delete=models.SET_NULL, null = True, related_name='nireden', blank=True)
    nira = models.ForeignKey(City, on_delete=models.SET_NULL, null = True, related_name='nira', blank=True)
    
    user_photo=ResizedImageField(size=[200, 200], quality=75,upload_to='user_photos/', blank=True, default='user_photo/default_taksist.png', force_format='PNG', null=True)
    car_photo=ResizedImageField(size=[200, 200], quality=75,upload_to='car_photos/', blank=True, default='car_photo/default_car.png', force_format='PNG', null=True)

    objects = models.Manager()

    def __str__(self) -> str:
        return self.user.first_name

    # def save(self, *args, **kwargs):
    #     super(TaxiProfile, self).save(*args, **kwargs)
    #     car_photo=Image.open(self.car_photo)
    #     if car_photo.width>100 or car_photo.height>100:
    #         photo_size=(100, 100)
    #         car_photo.thumbnail(photo_size)
    #         car_photo.save(self.car_photo.url)
