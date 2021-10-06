from typing import List
from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .forms import SellingCarForm
from .models import SellCar
# Create your views here.


class SellingCarsListView(ListView):
    model = SellCar
    context_object_name = "car"
    template_name = "buy/index.html"


class SellingCreateView(CreateView):
    model = SellCar
    template_name = "buy/create.html"
    form_class = SellingCarForm
