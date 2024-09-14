from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views import generic, View
from posters.models import Poster
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse

def view_cart(request):
    ''' Display the shopping cart ''' 
    return render(request, 'cart/cart.html')

   
def add_to_cart(request, article_id):
    ''' Add articles to the shopping cart '''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None

    if 'color_option' in request.POST:
        color = request.POST['color_option']
    cart = request.session.get('cart', {})

    if color:
        if article_id in list(cart.keys()):
            if color in cart[article_id]['items_by_color'].keys():
                messages.success(request, f'Poster added to your shopping cart. 1')
            else:
                cart[article_id]['items_by_color'][color] = quantity
                messages.success(request, f'Poster added to your shopping cart. 2')
        else: cart[article_id] = {'items_by_color': {color: quantity}}

    else:
        if article_id in list(cart.keys()):
            messages.success(request, f'Poster added to your shopping cart. 3')
        else:
            cart[article_id] = quantity
            messages.success(request, f'Poster added to your shopping cart. 4')

    request.session['cart'] = cart
    messages.success(request, f'Poster added to your shopping cart. 5')
    return redirect(redirect_url)


def delete_from_cart(request, article_id):
    ''' Delete article from shopping cart '''

    poster = get_object_or_404(Poster, pk=article_id)
    color = None
    if 'color_option' in request.POST:
        color = request.POST['color_option']
    cart = request.session.get('cart', {})

    if color:
        del cart[article_id]['items_by_color'][color]
        if not cart[article_id]['items_by_color']:
            cart.pop(article_id)
            messages.success(request, f'Removed poster from your cart')
    else:
        cart.pop(article_id)
        messages.success(request, f'Removed poster from your cart')

    request.session['cart'] = cart
    messages.success(request, f'Removed poster from your cart')
    return render(request, 'cart/cart.html', {'cart': cart,})


def edit_cart(request, article_id):
    ''' Change the color of the poster '''

    poster = get_object_or_404(Poster, pk=article_id)
    quantity = int(request.POST.get('quantity'))
    color = None
    # COLOR OPTION IS CURRENTLY NOT IN USE - feature left to implement
    if 'color_option' in request.POST:
        color = request.POST['color_option']
    cart = request.session.get('cart', {})

    if color:
        if quantity > 0:
            cart[article_id]['items_by_color'][color] = quantity
            messages.success(request, f'Updated cart')
        else:
            del cart[article_id]['items_by_color'][color]
            if not cart[article_id]['items_by_color']:
                cart.pop(article_id)
                messages.success(request, f'Removed poster from your cart')
    else:
        if quantity > 0:
            cart[article_id] = quantity
        else:
            cart.pop(article_id)
            messages.success(request, f'Removed poster from your cart')

    request.session['cart'] = cart
    return render(request, 'cart.html', {'cart': cart,})
    