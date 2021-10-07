from django.urls import path
from . import views

app_name = "sell"

urlpatterns = [
    path('',views.SellingCreateView.as_view(),name="index"),
]

