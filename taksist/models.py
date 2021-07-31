from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

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

# class TaxiCategory(models.Model):
#     taxi_category=[
#     ('Şäher Arasy', 'Şäher ara gatnaýaryn.'),
#     ('Şäher Içi', 'Diňe şäher içinde işleýärin.'),
#     ('Etrap Obalary', 'Etrabyň obalaryna gatnaýaryn.')]
 
#     user_id=models.OneToOneField(User, on_delete=models.CASCADE, related_name='name')
#     name=models.CharField(max_length=255, choices=taxi_category)
#     objects = models.Manager()
    
#     def __str__(self):
#         return self.name


# class TaxiStatus(models.Model):

#     taxi_status=[
#         ('Işde', 'Işe çykdym, işläp ýörün.'),
#         ('Dynçda', 'Şu wagt işlämok, dynç alýaryn.')
#     ]

#     user_id=models.OneToOneField(User, on_delete=models.CASCADE)
#     status=models.CharField(max_length=50, choices=taxi_status)
#     objects = models.Manager()

#     def __str__(self):
#         return self.status

class TaxiProfile(models.Model):
    category_choice = [(x.id, x.name) for x in Category.objects.all()]
    status_choice = [(x.id, x.name) for x in Status.objects.all()]
    city_choice1 = [(x.id, x.name) for x in City.objects.filter(id__gt=2)]
    city_choice2 = [(x.id, x.name) for x in City.objects.all()]

    user_id=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    mobile=models.CharField(max_length=13)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, choices=category_choice, blank=True)
    status = models.ForeignKey(Status, on_delete = models.SET_NULL, null = True, choices=status_choice, blank=True)
    nireden = models.ForeignKey(City, on_delete=models.SET_NULL, null = True, related_name='nireden1', choices=city_choice1, blank=True)
    nira = models.ForeignKey(City, on_delete=models.SET_NULL, null = True, related_name='nira1', choices=city_choice2, blank=True)
    
    car_photo=ResizedImageField(size=[100, 100], quality=75,upload_to='car_photos/', blank=True, default='car_photo/default_car.png')
    user_photo=ResizedImageField(size=[100, 100], quality=75,upload_to='user_photos/', blank=True, default='user_photo/default_taksist.png')

    objects = models.Manager()

    

    # def get_status(self):
    #     try:
    #         xstatus=TaxiStatus.objects.get(user_id=self.user_id)
    #         return xstatus.status
    #     except:
    #         return "tapylmady"
        
    # def get_category(self):
    #     try:
    #         xcategory = TaxiCategory.objects.get(user_id=self.user_id)
    #         return xcategory.name
    #     except:
    #         return "No Category"


    def save(self, *args, **kwargs):
        super(TaxiProfile, self).save(*args, **kwargs)
        car_photo=Image.open(self.car_photo.path)
        if car_photo.height>100 or car_photo.weight>100:
            photo_size=(100, 100)
            car_photo.thumbnail(photo_size)
            car_photo.save(self.car_photo.path)

# class SaherAra(models.Model):
#     cities = list((x.id, x.name) for x in City.objects.all())

#     user_id = models.OneToOneField(User, on_delete=models.CASCADE)
#     taxi_id = models.OneToOneField(TaxiProfile, on_delete=models.CASCADE)
#     city1 = models.ForeignKey(City, on_delete=models.CASCADE, choices=cities, related_name='nireden')
#     city2 = models.ForeignKey(City, on_delete=models.CASCADE, choices=cities, related_name='nira')
#     # city1 = models.CharField(max_length=20, choices=cities)
#     # city2 = models.CharField(max_length=20, choices=cities)

#     def __str__(self):
#         return '{} - {}'.format(self.city1, self.city2)

# class SaherIci(models.Model):
#     cities = list((x.id, x.name) for x in City.objects.all())

#     user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='haysy_saher')
#     taxi_id = models.OneToOneField(TaxiProfile, on_delete=models.CASCADE)
#     city = models.CharField(max_length=20, choices=cities)

#     def __str__(self):
#         return '{} - {}'.format(self.city, 'Saher ici')

# class EtrapObalary(models.Model):
#     cities = list((x.id, x.name) for x in City.objects.all())

#     user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='haysy_etrap')
#     taxi_id = models.OneToOneField(TaxiProfile, on_delete=models.CASCADE)
#     city = models.CharField(max_length=20, choices=cities)
    
#     def __str__(self):
#         return '{} - {}'.format(self.city, 'Etrap Obalary')