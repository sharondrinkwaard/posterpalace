from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Poster, Category


def all_posters(request):
    """ A view to display all posters on a page """

    posters = Poster.objects.all()
    categories = None
    query = None

    # Gets the category/search request and displays the correct products
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posters = posters.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'request' in request.GET:
            query = request.GET['request']
            if not query:
                messages.error(request, 'Enter search criteria')
                return redirect(reverse('posters'))

            # Queries in name OR description instead of both
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # Filters out the queries so only queries are displayed
            posters = posters.filter(queries)

    context = {
        'posters': posters,
        'search_request': query,
        'current_cat': categories,
    }

    return render(request, 'posters/posters.html', context)

def poster_detail(request, product_id):
    """ A view to show individual product details """

    poster = get_object_or_404(Product, pk=product_id)
    form_color = ProductColor()

    context = {
        'poster': poster,
        'form_color': form_color,
        }

    return render(request, 'posters/posters.html', context)

class Color(View):
    def post_color(self, request):
            c = ProductSize(request.POST)
            if c.is_valid():
                add_c = c.save(commit=False)
                add_c.save()
                return redirect('redirect_url')
            else:
                render(request, 'posters.html', {'c': c})
