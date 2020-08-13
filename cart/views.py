from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from programs.models import Program


# Create your views here.
@ login_required
def view_cart(request):

    # loading the content of the 'shopping_cart' from the session
    cart = request.session.get("shopping_cart", {})
    total = 0
    for k, v in cart.items():
        # have to convert back to float because
        # session can only store strings
        total += float(v["fees"]) * int(v["qty"])

    return render(request, "cart/view_cart.template.html", {
        "cart": cart,
        "total": total
    })


@ login_required
def add_to_cart(request, program_id):

    # the cart object is a dictionary
    cart = request.session.get("shopping_cart", {})

    # check if the program_id I want to add already exists inside the cart
    # if the program is not in the shopping cart
    if program_id not in cart:
        program = get_object_or_404(Program, pk=program_id)

        # add the program to cart
        cart[program_id] = {
            "id": program_id,
            "title": program.title,
            "date": str(program.date),
            "fees": float(program.fees),
            "qty": 1,
            "total_fees": float(program.fees)
        }
        messages.success(
            request, f"Added program '{program.title}' to the shopping cart")
    else:
        # if the program already exists in the cart
        cart[program_id]["qty"] += 1

    # save the shopping cart back to session
    request.session["shopping_cart"] = cart
    # after add to cart, let customer stay at all programs page
    programs = Program.objects.all()
    return render(request, "programs/all_programs.template.html", {
        "programs": programs
    })


@ login_required
def remove_from_cart(request, program_id):
    cart = request.session["shopping_cart"]
    if program_id in cart:

        # removew from the cart
        del cart[program_id]

        # save back the shopping cart into the session
        request.session["shipping_cart"] = cart
        messages.success(request, "The program has been removed")
    return redirect(reverse("view_cart"))


@ login_required
def update_cart_quantity(request, program_id):

    # get the shopping cart
    cart = request.session["shopping_cart"]
    if program_id in cart:

        # update the quantity
        cart[program_id]['qty'] = request.POST['qty']
        cart[program_id]['total_fees'] = int(request.POST['qty']) * float(cart[program_id]['fees'])

        # save the cart back into the session
        request.session["shopping_cart"] = cart
        messages.success(request, f"Quantity for {cart[program_id]['title']} has been updated")
        return redirect(reverse("view_cart"))
    else:
        messages.success(request, "The program doesn't exist in your cart.")
        return redirect(reverse('view_cart'))
