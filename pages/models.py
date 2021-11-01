from django.db import models

from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class CampaignsModel(models.Model):
    """Model definition for CampaignsModel."""

    # TODO: Define fields here
    campain = models.CharField(verbose_name="campaign name", max_length=120)
    slogan = models.CharField(verbose_name="slogan", max_length=120)
    image = models.ImageField(upload_to = 'advert/image/',help_text="Height and width must be 1000px x 1000px")
    active = models.BooleanField(default=False,verbose_name="is active")
    slug = models.SlugField(_("slug"),editable=False,blank=True,null=True)    


    class Meta:
        """Meta definition for CampaignsModel."""
    
        verbose_name = 'Campaigns model'
        verbose_name_plural = 'Campaigns models'

    def __str__(self):
        return self.campain

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.campain)
        super(CampaignsModel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for CampaignsModel."""
        return ('')

    # TODO: Define custom methods here
