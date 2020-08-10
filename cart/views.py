from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.contrib import messages
from programs.models import Program
# import json
# from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.
def view_cart(request):
    cart = request.session["shopping_cart"]
    total = 0
    for k, v in cart.items():
        total += float(v["fees"]) * int(v["qty"])

    return render(request, "cart/view_cart.template.html", {
        "cart": cart,
        "total": total
    })


def add_to_cart(request, program_id):
    cart = request.session.get("shopping_cart", {})
    if program_id not in cart:
        program = get_object_or_404(Program, pk=program_id)
        # program.date = json.dumps(Program.date, cls=DjangoJSONEncoder)
        cart[program_id] = {
            "id": program_id,
            "title": program.title,
            # "date": program.date,
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


def remove_from_cart(request, program_id):
    cart = request.session["shopping_cart"]
    if program_id in cart:
        del cart[program_id]
        request.session["shipping_cart"] = cart
        messages.success(request, "The program has been removed")
    return redirect(reverse("view_cart"))


def update_cart_quantity(request, program_id):
    cart = request.session["shopping_cart"]
    if program_id in cart:
        cart[program_id]['qty'] = request.POST['qty']
        cart[program_id]['total_fees'] = int(request.POST['qty']) * float(cart[program_id]['fees'])
        request.session["shopping_cart"] = cart
        messages.success(request, f"Quantity for {cart[program_id]['title']} has been updated")
        return redirect(reverse("view_cart"))
    else:
        messages.success(request, "The program doesn't exist in your cart.")
        return redirect(reverse('view_cart'))
