from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    # path('safe_payment_data/', views.safe_payment_data, name='safe_payment_data'),
    # path('wh/', webhook, name='webhook'),
]
