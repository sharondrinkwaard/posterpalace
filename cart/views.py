from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from posters.models import Poster


def view_cart(request):
    """ Display the shopping cart """
    return render(request, 'cart/cart.html')

def add_to_cart(request, article_id):
    """ Add articles to the shopping cart """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    color = None

    if 'color_option' in request.POST:
        color = request.POST['color_option']

    request.session['cart'] = cart
    return redirect(redirect_url)

def delete_from_cart(request, article_id):
    """ Delete article from shopping cart """

    poster = get_object_or_404(Poster, pk=article_id)
    color = None
    if 'color_option' in request.POST:
        color = request.POST['color_option']
    cart = request.session.get('cart', {})

    if color:
        del cart[article_id]['items_by_color'][size]
        if not cart[article_id]['items_by_color']:
            cart.pop(article_id)
        # messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
    else:
        cart.pop(article_id)
        # messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return HttpResponse(status=200)
    