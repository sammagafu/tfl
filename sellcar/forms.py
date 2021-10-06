from django import forms
from . models import SellCar

class SellingCarForm(forms.ModelForm):
    
    class Meta:
        model = SellCar
        fields = '__all__'
