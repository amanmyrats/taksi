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
        self.fields['mobile'].widget.attrs={
            'class': 'form-control item'
        }
        self.fields['category'].widget.attrs={
            'class': 'form-control item'
        }
        self.fields['status'].widget.attrs={
            'class': 'form-control item'
        }
        self.fields['nireden'].widget.attrs={
            'class': 'form-control item'
        }
        self.fields['nira'].widget.attrs={
            'class': 'form-control item'
        }


class UserModelForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs={
            'class': 'form-control item'
        }
        self.fields['last_name'].widget.attrs={
            'class': 'form-control item'
        }