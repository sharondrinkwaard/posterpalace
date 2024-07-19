from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    # path('payment_succes/<order_number>', views.payment_succes, name='payment_succes'),
    # path('safe_payment_data/', views.safe_payment_data, name='safe_payment_data'),
    # path('wh/', webhook, name='webhook'),
]
