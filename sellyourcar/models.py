from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class ClientCar(models.Model):
    Make = [
        ('Toyota','Toyota'),
        ('Audi','Audi'),
        ('BMW','BMW'),
        ('Chevrolet','Chevrolet'),
        ('Ford','Ford'),
        ('Honda','Honda'),
        ('Jaguar','Jaguar'),
        ('KIA','KIA'),
        ('Lexus','Lexus'),
        ('Mazda','Mazda'),
        ('Mercedes','Mercedes'),
        ('Porsche','Porsche'),
        ('Others','Others'),
    ]

    CAR_TRANSMISSION = [
        ('AT','AUTOMATIC'),('Mn','Manual')
    ]

    firstname = models.CharField(max_length=50,verbose_name=_("First name"))
    lastname = models.CharField(max_length=50,verbose_name=_("Last name"))
    phone  = models.CharField(max_length=14,verbose_name="Phone number")
    email = models.EmailField(_(""), max_length=254,unique=True)
    registration = models.CharField(max_length=50,verbose_name=_("Registratin Number"),help_text="Eg T 123 DGV")
    registration_year = models.IntegerField(_("Year of registratin"),help_text="Eg 2008")
    make = models.CharField(max_length=50,choices=Make,verbose_name=_("Make"))
    model = models.CharField(max_length=50,verbose_name=_("Make"),help_text="Eg Crown")
    milage = models.IntegerField(_("Mileage"))
    color = models.CharField(max_length=50,verbose_name=_("Color"),help_text="Eg Dark Blue")
    trans = models.CharField(max_length=50,verbose_name=_("Transmission"),choices=CAR_TRANSMISSION)
    price = models.IntegerField(verbose_name=_("Expected Price in TSH"))
    description = models.TextField(_("Car description"))
    addion = models.TextField(_("Addion Details"))


    

    class Meta:
        verbose_name = _("Car for sale")
        verbose_name_plural = _("Cars for sale")

    def __str__(self):
        return "{} {} {}".format(self.make,self.model,self.price)

    def get_absolute_url(self):
        return reverse("ClientCars_detail", kwargs={"pk": self.pk})
