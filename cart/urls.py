# from django.contrib import admin
from django.urls import path
import cart.views

urlpatterns = [
    path("add/<program_id>", cart.views.add_to_cart, name="add_to_cart"),
    path("view", cart.views.view_cart, name="view_cart"),
    path("remove/<program_id>", cart.views.remove_from_cart,
         name="remove_from_cart"),
]
