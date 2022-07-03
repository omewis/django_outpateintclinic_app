from django.contrib import admin

# Register your models here.
from .models import Booking,doctor,clinic,clininfo,num_of_building

admin.site.register((Booking,doctor,clinic,clininfo,num_of_building,))
