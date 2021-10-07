from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ClientCarForm

# Create your views here.
from .models import ClientCars

class SellingCreateView(CreateView):
    model = ClientCars
    template_name = "buy/create.html"
    form_class = ClientCarForm