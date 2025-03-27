from django.shortcuts import render
from .models import Farmer, Crop, Order

def home(request):
    return render(request, 'farmers/home.html')

def farmer_list(request):
    farmers = Farmer.objects.all()
    return render(request, 'farmers/farmer_list.html', {'farmers': farmers})

def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'farmers/crop_list.html', {'crops': crops})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'farmers/order_list.html', {'orders': orders})

def farmers_list(request):
    farmers = Farmer.objects.all()  # Get all farmers from DB
    return render(request, 'farmers_list.html', {'farmers': farmers})

def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'farmers/crop_list.html', {'crops': crops})