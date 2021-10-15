from django.shortcuts import render
from .models import Restaurant
import random


def choose_random_restaurant(restaurants):
    number_of_restaurants = len(restaurants)
    chosen_index = random.randint(0, number_of_restaurants - 1)
    return restaurants[chosen_index]


def main_picker(request):
    restaurant_list = Restaurant.objects.all()
    random_restaurant = choose_random_restaurant(restaurant_list)
    return render(request, 'restaurantpicker/main_picker.html', {'random_restaurant': random_restaurant})
