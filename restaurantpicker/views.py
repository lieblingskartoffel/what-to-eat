from django.shortcuts import render


def main_picker(request):
    return render(request, 'restaurantpicker/main_picker.html')
