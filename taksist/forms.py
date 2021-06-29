from django import forms

from .models import TaxiProfile, Category, City #, TaxiStatus, TaxiCategory
from django.contrib.auth.models import User

class TaxiProfileModelForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     super(FooForm, self).__init__(*args, **kwargs)
    #     self.fields['bar_field'].choices = create_complex_choices(self.instance)


    # def __init__(self, *args, **kwargs):
    #     super (TaxiProfileModelForm, self).__init__(*args, **kwargs)
    #     self.fields['nireden'].choices =[(1,'test1'), (2,'test2')]
    #     self.fields['nira'].queryset = City.objects.all()
    # nireden = forms.ModelChoiceField(queryset=City.objects.all())
    class Meta:
        model=TaxiProfile
        fields=['car_photo', 'user_photo', 'mobile', 'category', 'status', 'nireden','nira']


# class TaxiCategoryModelForm(forms.ModelForm):
#     class Meta:
#         model=TaxiCategory
#         fields=['name']


# class TaxiStatusModelForm(forms.ModelForm):
#     class Meta:
#         model=TaxiStatus
#         fields=['status']


class UserModelForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name']