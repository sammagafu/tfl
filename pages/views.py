from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from .forms import AppointmentForm


class Homepage(TemplateView):
    template_name = "pages/index.html"

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