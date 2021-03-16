from django import forms

from .models import TaxiProfile , TaxiStatus, TaxiCategory
from django.contrib.auth.models import User

class TaxiProfileModelForm(forms.ModelForm):
    class Meta:
        model=TaxiProfile
        fields=['car_photo', 'user_photo', 'mobile']


class TaxiCategoryModelForm(forms.ModelForm):
    class Meta:
        model=TaxiCategory
        fields=['name']


class TaxiStatusModelForm(forms.ModelForm):
    class Meta:
        model=TaxiStatus
        fields=['status']


class UserModelForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name']