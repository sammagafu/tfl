from django.contrib import admin
from . models import ClientCar
# Register your models here.


@admin.register(ClientCar)
class ClientCarAdmin(admin.ModelAdmin):
    pass


