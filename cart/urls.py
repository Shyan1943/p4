# from django.contrib import admin
from django.urls import path
import cart.views

urlpatterns = [
    path('add/<program_id>', cart.views.add_to_cart, name="add_to_cart"),
]
