from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from django.contrib.sites.models import Site
from django.conf import settings
import stripe
from programs.models import Program


def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('shopping_cart', {})
    line_items = []

    all_program_ids = []

    for program_id, program in cart.items():
        program_model = get_object_or_404(Program, pk=program_id)
        item = {
            "name": program_model.title,
            "amount": int(program_model.fees * 100),
            "quantity": program['qty'],
            "currency": "usd",
        }

        line_items.append(item)
        all_program_ids.append(str(program_model.id))

    current_site = Site.objects.get_current()
    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })

def checkout_success(request):
    return HttpResponse("checkout success")


def checkout_cancelled(request):
    return HttpResponse("checkout cancelled")
