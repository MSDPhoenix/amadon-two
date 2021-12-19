from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout/', views.checkout),
    path('display_checkout_page/', views.display_checkout_page),
]
