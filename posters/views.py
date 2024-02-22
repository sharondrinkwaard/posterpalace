from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Poster


def all_posters(request):
    """ A view to display all posters on a page """

    posters = Poster.objects.all()

    context = {
        'posters': posters,
    }

    return render(request, 'posters/posters.html')
