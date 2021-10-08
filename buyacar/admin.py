from django.contrib import admin
from . models import CarModel,CarFeatures,BuyACar,Category,CarColor,CarImage
# Register your models here.

admin.site.register(Category)
admin.site.register(CarModel)
admin.site.register(CarFeatures)
admin.site.register(CarColor)

class CarImageInline(admin.StackedInline):
    model = CarImage

@admin.register(BuyACar)
class BuyACarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
