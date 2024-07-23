from django.conf import settings
from .forms import OrderForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from cart.contexts import shopping_content
import stripe
from posters.models import Poster
from .models import Order, OrderLineItem


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'date': request.POST['date'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for article_id, article_data in cart.items():
                try:
                    poster = Poster.objects.get(id=article_id)
                    if isinstance(article_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            poster=poster,
                            quantity=article_data,
                        )
                        order_line_item.save()
                    else:
                        for color, quantity in article_data['items_by_color'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                poster=poster,
                                quantity=quantity,
                                poster_color=poster_color,
                            )
                            order_line_item.save()
                except Poster.DoesNotExist:
                    messages.error(request, (
                        'This product is not available anymore. Contact us for more info'
                    ))
                    order.delete()
                    return redirect(reverse('view_cart'))
            request.session['save_info'] = save_info in request.POST
            return redirect(reverse('checkout_succes', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart")
            return redirect(reverse('posters'))

        current_cart = shopping_content(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
        
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ Handle successful checkouts """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

