from django import forms
from . models import ClientCar

class ClientCarForm(forms.ModelForm):
    
    class Meta:
        model = ClientCar
        fields = '__all__'
