from django.contrib import admin

# Register your models here.

from .models import Tour, TourPackage

admin.site.register(Tour)
admin.site.register(TourPackage)
