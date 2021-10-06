from typing import List
from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import SellCar
# Create your views here.


class SellingCarsListView(ListView):
    model = SellCar
    template_name = "sell/index.html"


class SellingCreateView(CreateView):
    model = SellCar
    template_name = "sell/create.html"
