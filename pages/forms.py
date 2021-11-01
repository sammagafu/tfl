from django import forms
from django.forms import ModelChoiceField
from  . models import CampaignsModel

class AppointmentForm(forms.Form):

    SALES = [

    ('20% off for service', '20% off for service'),
    ('10% off for body work', '10% off for body work'),

    ]

    name = forms.CharField()
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    offer = forms.ModelChoiceField(queryset=CampaignsModel.objects.all(), initial=0)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass