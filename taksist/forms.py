from django import forms

from .models import TaxiProfile, Category, City
from django.contrib.auth.models import User

class TaxiProfileModelForm(forms.ModelForm):

    class Meta:
        model=TaxiProfile
        fields=['car_photo', 'user_photo', 'mobile', 'category', 'status', 'nireden','nira']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nireden'].queryset = City.objects.all().exclude(id=1).exclude(id=2)

class UserModelForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name']