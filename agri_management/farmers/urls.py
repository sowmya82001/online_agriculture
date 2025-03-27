from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('farmers/', views.farmer_list, name='farmer_list'),
    path('crops/', views.crop_list, name='crop_list'),
    path('orders/', views.order_list, name='order_list'),
    
]
