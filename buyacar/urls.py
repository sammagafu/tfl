from django.urls import path
from . import views

app_name = "buy"

urlpatterns = [
    path('',views.SellingCarsListView.as_view(),name="index"),
    path('?<make>',views.GetCarsByMake.as_view(),name="make"),
    path('<int:pk>',views.SellingCarrsDetail.as_view(),name="detail"),
    path('add/',views.SellingCreateView.as_view(),name="create")
]