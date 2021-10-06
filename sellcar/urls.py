from django.urls import path
from . import views

app_name = "buy"

urlpatterns = [
    path('buy/',views.SellingCarsListView.as_view(),name="index"),
    path('add/',views.SellingCreateView.as_view(),name="create")
]
