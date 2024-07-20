from django.conf import settings
from .forms import OrderForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart")
        return redirect(reverse('posters'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51McQpqGL29wYvReMN5NRcKhCFIuOHM7YVGCyeaPx9ylJIKcwerMaSeEw56Ww8aQfTeWobAedsQguQzNQGku1iDGn00X6cduK9s',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

