from django.contrib import admin
from .models import CarModel,CarFeatures,SellCar



# Register your models here.
admin.site.register(CarModel)
admin.site.register(CarFeatures)
admin.site.register(SellCar)