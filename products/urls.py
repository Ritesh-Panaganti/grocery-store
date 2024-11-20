from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("history/", views.history),
    path('cart/', views.cart),
    path('thank_you/', views.thank_you),
]