from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View


def view_cart(request):
    """ A view to display the shopping cart """
    return render(request, 'cart/cart.html')

def add_to_cart(request, article_id):
    """ A view to add articles to the shopping cart """
    # quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')  --- not neccesary?
    cart = request.session.get('cart', {})
    color = None

    if 'color_option' in request.POST:
        color = request.POST['color_option']

    request.session['cart'] = cart
    return redirect(redirect_url)
    