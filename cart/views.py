from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from programs.models import Program


# Create your views here.
def add_to_cart(request, program_id):
    cart = request.session.get("shopping_cart", {})
    if program_id not in cart:
        program = get_object_or_404(Program, pk=program_id)
        cart[program_id] = {
            "id": program_id,
            "title": program.title,
            "fees": 500,
            'qty': 1
        }
    else:
        cart[program_id]['qty'] += 1
    request.session["shopping_cart"] = cart
    return HttpResponse("Pro added")
