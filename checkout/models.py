from django.db import models
from posters.models import Poster
from django.conf import settings
from django.db.models import Sum
import uuid


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # stripe_pid = models.CharField(max_length=260, null=False, blank=False, default='')
    # original_cart = models.TextField(null=False, blank=False, default='')

    def _create_order_number(self):
        """ Creates a unique order number using UUID """
        return uuid.uuid4().hex.upper()
    
    # DO I NEED THIS? ---->> maybe delete?
    # There are no delivery costs
    def update_total(self):
        """ Update grand total each time a line item is added """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        # if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
        #     self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        # else:
        #     self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_costs
        self.save()
    
    def save(self, *args, **kwargs):
        """ Override the original save method to set the order number if there is none """
        if not self.order_number:
            self.order_number = self._create_order_number()
        super().save(*args, **kwargs)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    poster = models.ForeignKey(Poster, null=False, blank=False, on_delete=models.CASCADE)
    poster_color = models.CharField(max_length=25, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.poster.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.poster.sku} on order {self.order.order_number}'


