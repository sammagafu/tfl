from django.urls import path
from . import views

app_name = "buy"

urlpatterns = [
    path('buy/',views.SellingCarsListView.as_view(),name="index"),
    path('buy/<int:pk>',views.SellingCarrsDetail.as_view(),name="detail"),
    path('add/',views.SellingCreateView.as_view(),name="create")
]
