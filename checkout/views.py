from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import stripe
from programs.models import Program
from .models import Purchase
from django.contrib.auth.models import User


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
        metadata={'all_programs_id': ",".join(all_program_ids)},
        client_reference_id=request.user.id,
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )

    return render(request, "checkout/checkout.template.html", {
        "session_id": session.id,
        "public_key": settings.STRIPE_PUBLISHABLE_KEY
    })

def checkout_success(request):
    return HttpResponse("checkout success")


def checkout_cancelled(request):
    return HttpResponse("checkout cancelled")


@csrf_exempt
def payment_completed(request):
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    endpoint_secret = settings.SIGNING_SECRET
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret)
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event['data']['object']
        handle_payment(session)

    return HttpResponse(status=200)


def handle_payment(session):
    user = get_object_or_404(User, pk=session["client_reference_id"])
    all_program_ids = session['metadata']['all_programs_id'].split(",")

    for program_id in all_program_ids:
        program_model = get_object_or_404(Program, pk=program_id)

        purchase = Purchase()
        purchase.program_id = program_model
        purchase.user_id = user
        purchase.save()
