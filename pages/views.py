from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from .forms import AppointmentForm
from buyacar.models import BuyACar,Category


class Homepage(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = BuyACar.objects.all()[:8]
        context["category"] = Category.objects.all()[:8]
        return context
    

class Contactpage(TemplateView):
    template_name = "pages/contact.html"

class AboutUs(TemplateView):
    template_name = "pages/about.html"

class ACService(TemplateView):
    template_name = "pages/service/ac.html"

class BrakeSuspension(TemplateView):
    template_name = "pages/service/brakes.html"

class CarDiagnosis(TemplateView):
    template_name = "pages/service/diagnosis.html"

class BodyWorkpaint(TemplateView):
    template_name = "pages/service/body.html"

class OriginalService(TemplateView):
    template_name = "pages/service/original.html"

class Insuarance(TemplateView):
    template_name = "pages/insuarance.html"

class Appointment(FormView):
    form_class = AppointmentForm
    template_name = "pages/appointment.html"
    success_url = '/thanks/'