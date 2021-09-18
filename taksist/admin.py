from django.contrib import admin

from .models import TaxiProfile, User, Category, City

admin.site.register( TaxiProfile )
admin.site.register( Category )
admin.site.register( City )