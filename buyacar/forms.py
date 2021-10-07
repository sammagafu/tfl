from django import forms
from . models import BuyACar

class SellingCarForm(forms.ModelForm):
    
    class Meta:
        model = BuyACar
        fields = '__all__'
