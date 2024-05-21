from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View


def index(request):
    """ A view to return the index page """
    return render(request, 'homepage/index.html')

def service(request):
    """ A view to direct to the customer service page """
    return render(request, 'service.html')
