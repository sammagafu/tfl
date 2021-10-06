from django.urls import path
from . import views
app_name = "page"

urlpatterns = [
    path('', views.Homepage.as_view(),name="home"),
    path('contact-us', views.Contactpage.as_view(),name="contact"),
    path('about-us', views.AboutUs.as_view(),name="about"),
]