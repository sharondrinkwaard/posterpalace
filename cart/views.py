from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View


def view_cart(request):
    """ A view to display the shopping cart """
    return render(request, 'cart/cart.html')
