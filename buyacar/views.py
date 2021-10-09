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
    model = BuyACar
    template_name = "buy/index.html"
    
    def get_queryset(self):
        name = self.kwargs.get('q', '')
        object_list = self.model.objects.all()
        print(name)
        if name:
            object_list = object_list.filter(name__icontains=name)
        return object_list
    


class SellingCarrsDetail(DetailView):
    model = BuyACar
    context_object_name = "car"
    template_name='buy/details.html'

class SellingCreateView(CreateView):
    model = BuyACar
    template_name = "buy/create.html"
    form_class = SellingCarForm