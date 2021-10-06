from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify

import os
from random import *


# Create your models here.
class CarModel(models.Model):
    brand = models.CharField(max_length=120,verbose_name=_("car brand name"))
    logo = models.ImageField(upload_to = 'car/logo/')
    slug = models.SlugField(_("slug"),editable=False,blank=True,null=True)    

    class Meta:
        verbose_name = _("Car Manufacture")
        verbose_name_plural = _("Cars Manufactures")

    def __str__(self):
        return self.brand

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand)
        super(CarModel, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("CarModel_detail", kwargs={"pk": self.pk})

class CarFeatures(models.Model):
    feature = models.CharField(max_length=50)
    slug = models.SlugField(_("slug"),editable=False,blank=True,null=True)   

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.feature)
        super(CarFeatures, self).save(*args, **kwargs) 

    def __str__(self):
        return self.feature

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")
    


class SellCar(models.Model):

    def photo_path(self,instance, filename):
        basefilename, file_extension= os.path.splitext(filename)
        chars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
        randomstr= ''.join((random.choice(chars)) for x in range(10))
        return 'images/{brand}/{basename}{randomstring}{ext}'.format(brand= self.brand, basename= basefilename, randomstring= randomstr, ext= file_extension)

    CAR_TRANSMISSION = [
        ('AT','AUTOMATIC'),('Mn','Manual')
    ]

    FUEL = (
        ('Petrol','Petrol'),
        ('Diesel','Diesel'),
        ('Gas','Gas'),
        ('Electric','Electric'),
        ('Hibrid','Hibrid')
    )

    HAND = (
        ('Left','Left'),
        ('Right','Right'),
        ('Default','Defaut'),
    )

    Drive = (
        ('2WD','2WD'),
        ('4WD','4WD'),
        ('AWD','AWD'),
    )


    brand = models.ForeignKey(CarModel, verbose_name=_("Brand Name"), on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'photo_path')
    model = models.CharField(max_length=50,verbose_name=_("Car Model"))
    color = models.CharField(max_length=50,verbose_name=_("Color of the car"),null=False,blank=False)
    trans = models.CharField(max_length=2,verbose_name=_("Transmision"),choices=CAR_TRANSMISSION)
    fuel  = models.CharField(max_length=12,verbose_name=_("Fuel"),choices=FUEL)
    mileage = models.IntegerField(verbose_name=_("Milage"),null=False,blank=False)
    engine = models.IntegerField(verbose_name=_("Engine size"),null=False,blank=False)
    registered = models.IntegerField(verbose_name=_("Registered Year"),null=False,blank=False)
    doors = models.IntegerField(verbose_name=_("Doors"),null=False,blank=False)
    seats = models.IntegerField(verbose_name=_("Seats"),null=False,blank=False)
    passenger = models.IntegerField(verbose_name=_("Passengers"),null=False,blank=False)
    body = models.IntegerField(verbose_name=_("Body"),null=False,blank=False)
    hand  = models.CharField(max_length=12,verbose_name=_("Driving Hand"),choices=HAND)
    drive  = models.CharField(max_length=12,verbose_name=_("Drive"),choices=Drive)
    available = models.BooleanField(_("Car is available"),default=True)
    features = models.ManyToManyField(CarFeatures,verbose_name=_("features"))
    
    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")

    def __str__(self):
        return self.brand


