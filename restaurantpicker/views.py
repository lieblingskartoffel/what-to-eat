from django.shortcuts import render
from .models import Restaurant


def main_picker(request):
    restaurant_list = Restaurant.objects.all()
    return render(request, 'restaurantpicker/main_picker.html', {'restaurants': restaurant_list})
