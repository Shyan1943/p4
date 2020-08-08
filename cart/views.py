from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib import messages
from programs.models import Program


# Create your views here.
def view_cart(request):
    cart = request.session["shopping_cart"]
    return render(request, "cart/view_cart.template.html", {
        "cart": cart
    })


def add_to_cart(request, program_id):
    cart = request.session.get("shopping_cart", {})
    if program_id not in cart:
        program = get_object_or_404(Program, pk=program_id)
        cart[program_id] = {
            "id": program_id,
            "title": program.title,
            "date": program.date,
            "fees": float(program.fees),
            "qty": 1,
            "total_fees": float(program.fees)
        }
        messages.success(
            request, f"Added program '{program.title}' to the shopping cart")
    else:
        cart[program_id]["qty"] += 1
    request.session["shopping_cart"] = cart
    return redirect(reverse(view_cart))
