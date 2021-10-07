from django import forms
from . models import ClientCars

class ClientCarForm(forms.ModelForm):
    
    class Meta:
        model = ClientCars
        fields = '__all__'
