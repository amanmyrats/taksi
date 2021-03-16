from django.contrib import admin

from .models import TaxiProfile , TaxiCategory, TaxiStatus

admin.site.register( TaxiProfile)
admin.site.register( TaxiCategory)
admin.site.register( TaxiStatus)