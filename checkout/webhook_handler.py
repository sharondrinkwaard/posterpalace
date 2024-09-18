from django.http import HttpResponse
from .models import Order, OrderLineItem
from posters.models import Poster
from profiles.models import UserProfile
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.core.files.storage import default_storage
from django.conf import settings
import stripe
import json
import time


class StripeWH_Handler:
    '''Handle Stripe webhooks'''

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        '''Send user a confirmation email with download link after ordering'''
        customer_email = order.email
        customer_name = order.first_name
        print("Sending confirmation email...")
        # Generate the link to the checkout_success page
        download_link = self.request.build_absolute_uri(
            reverse('checkout_success', args=[order.order_number])
        )

        # Email subject and body
        subject = render_to_string(
            'checkout/confirmation_email/confirmation_email_subject.txt',
            {'order': order}
        )
        body = render_to_string(
            'checkout/confirmation_email/confirmation_email_body.txt',
            {
                'order': order,
                'customer_name': customer_name,
                'download_link': download_link,
            }
        )

        # Create and send the email
        email = EmailMessage(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email],
        )

        try:
            email.send(fail_silently=False)
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    def handle_event(self, event):
        '''Handle a generic/unknown/unexpected webhook event'''
        return HttpResponse(
            content=f'unhandled Webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        '''Handle the payment_intent.succeeded webhook from Stripe'''
        print("Webhook event received: payment_intent.succeeded")
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
        intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        total = round(stripe_charge.amount / 100, 2)

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_first_name = billing_details.first_name
                profile.default_last_name = billing_details.last_name
                profile.default_phone_number = billing_details.phone
                profile.default_email = billing_details.email
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=billing_details.name,
                    last_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    order_total=total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]} | SUCCESS: '
                         'Verified order already in database'),
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name__iexact=billing_details.name,
                    last_name__iexact=billing_details.name,
                    user_profile=profile,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    order_total=total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for article_id, article_data in json.loads(cart).items():
                    poster = Poster.objects.get(id=item_id)
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
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: '
                     'Created order in webhook'),
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)