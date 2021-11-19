from django.urls import path
from . import views
app_name = "page"

urlpatterns = [
    path('', views.Homepage.as_view(),name="home"),
    path('contact-us', views.Contactpage.as_view(),name="contact"),
    path('about-us', views.AboutUs.as_view(),name="about"),
    path('insuarance', views.Insuarance.as_view(),name="insuarance"),
    path('appointment', views.Appointment.as_view(),name="appointment"),
    path('service', views.Service.as_view(),name="service"),
    path('service/air-condition', views.ACService.as_view(),name="ac"),
    path('service/brake-suspension', views.BrakeSuspension.as_view(),name="brakes"),
    path('service/car-diagnosis', views.CarDiagnosis.as_view(),name="diagnosis"),
    path('service/body-work-and-paint', views.BodyWorkpaint.as_view(),name="body"),
    path('service/car-service', views.OriginalService.as_view(),name="original"),
    path('service/original-spare-parts', views.SpareParts.as_view(),name="spare"),
]