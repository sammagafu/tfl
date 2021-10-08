from django.urls import path
from . import views
app_name = "page"

urlpatterns = [
    path('', views.Homepage.as_view(),name="home"),
    path('contact-us', views.Contactpage.as_view(),name="contact"),
    path('about-us', views.AboutUs.as_view(),name="about"),
    path('insuarance', views.Insuarance.as_view(),name="insuarance"),
    path('service/air-condition', views.ACService.as_view(),name="ac"),
    path('service/brake-suspension', views.BrakeSuspension.as_view(),name="brakes"),
    path('service/car-diagnosis', views.CarDiagnosis.as_view(),name="diagnosis"),
    path('service/body-work-and-paint', views.BodyWorkpaint.as_view(),name="body"),
    path('service/original-service-parts', views.OriginalService.as_view(),name="original"),
]