from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant


def vse_menu(request):
    page='vse_menu'
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return render(request, 'menu/vse_menu.html', context)

def one_menu(request, id):
    page = 'one_menu'
    restaurant = Restaurant.objects.get(id=id)
    context = {'restaurant':restaurant}
    return render(request, 'menu/one_menu.html', context)




