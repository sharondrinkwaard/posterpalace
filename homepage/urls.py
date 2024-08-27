from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('homepage/', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact_view, name='contact'),
]