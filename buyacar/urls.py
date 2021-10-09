from django.urls import path,re_path
from . import views

app_name = "buy"

urlpatterns = [
    path('',views.SellingCarsListView.as_view(),name="index"),
    path('<str:slug>',views.GetCarsByMake.as_view(),name="make"),
    path('filter/<str:slug>',views.GetCarsByColor.as_view(),name="color"),
    # re_path(r'^(?P<slug>\D+)',views.GetCarsByMake.as_view(),name="make"),
    path('<int:pk>',views.SellingCarrsDetail.as_view(),name="detail"),
    path('add/',views.SellingCreateView.as_view(),name="create")
]