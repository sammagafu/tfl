from django.urls import path
from . import views

app_name = "buy"

urlpatterns = [
    path('',views.SellingCarsListView.as_view(),name="index"),
    path('create/',views.SellingCreateView.as_view(),name="create")
]
