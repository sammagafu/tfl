from django.shortcuts import render
from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = "pages/index.html"

class Contactpage(TemplateView):
    template_name = "pages/contact.html"

class AboutUs(TemplateView):
    template_name = "pages/about.html"