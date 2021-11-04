from django.db.models import query
from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from .forms import SellingCarForm
from .models import BuyACar,Category,CarFeatures,CarColor
# Create your views here.


class SellingCarsListView(ListView):
    model = BuyACar
    context_object_name = "cars"
    template_name = "buy/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["feature"] = CarFeatures.objects.all()
        context["color"] = CarColor.objects.all()
        return context

class GetCarsByMake(ListView):
    model = Category
    template_name = "buy/filters.html"
    context_object_name = "cars"

    
    def get_queryset(self):
        name = self.kwargs['slug']
        object_list = self.model.objects.all()
        if name:
            object_list = object_list.filter(slug__icontains=name).get()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["feature"] = CarFeatures.objects.all()
        context["color"] = CarColor.objects.all()
        return context

class GetCarsByColor(ListView):
    model = CarColor
    template_name = "buy/filters.html"
    context_object_name = "cars"

    
    def get_queryset(self):
        name = self.kwargs['slug']
        object_list = self.model.objects.all()
        if name:
            object_list = object_list.filter(slug__icontains=name).get()
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["feature"] = CarFeatures.objects.all()
        context["color"] = CarColor.objects.all()
        return context
        

class SellingCarrsDetail(DetailView):
    model = BuyACar
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    context_object_name = "car"
    template_name='buy/details.html'

class SellingCreateView(CreateView):
    model = BuyACar
    template_name = "buy/create.html"
    form_class = SellingCarForm

class FilterStatus(ListView):
    model = BuyACar
    template_name = "buy/filters.html"
    context_object_name = "cars"

    def get_queryset(self):
        return self.model.objects.all().filter(car_status="Used Japan").get()