from django.shortcuts import render, get_object_or_404, HttpResponse, reverse, redirect
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# import in the settings
from django.conf import settings

# import in stripe
import stripe

# import in the Program
from programs.models import Program

# import in the purchase
from .models import Purchase
from django.contrib.auth.models import User


@login_required
def checkout(request):
    # tell Stripe what my api_key is
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # retrieve my shopping cart
    cart = request.session.get('shopping_cart', {})

    # create our line items
    line_items = []

    # stores all the ids of the programs which we are purchasing
    all_program_ids = []

    # go through each program in the shopping cart
    for program_id, program in cart.items():
        # retrieve the program by its id from the database
        program_model = get_object_or_404(Program, pk=program_id)

        # create line item
        # you see all the possible properties of a line item at:
        # https://stripe.com/docs/api/invoices/line_item
        item = {
            "name": program_model.title,
            "amount": int(program_model.fees * 100),
            "quantity": program['qty'],
            "currency": "usd",
        }

        line_items.append(item)
        all_program_ids.append(str(program_model.id))

    # get our current domain
    current_site = Site.objects.get_current()

    # get the domain name
    domain = current_site.domain

    # create a payment session to represent the current transaction
    session = stripe.checkout.Session.create(

        # take credit cards
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


@login_required
def checkout_success(request):
    request.session["shopping_cart"] = {}
    messages.success(request, "Your purchases been completed")
    return redirect(reverse('all_programs_route'))


@login_required
def checkout_cancelled(request):
    messages.error(request, "Payment has been cancelled.")
    return redirect(reverse('all_programs_route'))


@login_required
@csrf_exempt
def payment_completed(request):

    # retrieve the information from the payment (also known as the payload)
    # this will contains the information sent out, like the line items
    payload = request.body

    # verify that the payment is legit
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    endpoint_secret = settings.SIGNING_SECRET
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret)
    except ValueError:
        # invalid payload
        # status 400 means forbidden (this means someone tried to s
        # poof a stripe payemnt)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # invalid signature
        return HttpResponse(status=400)

    # handle the payment proper
    if event["type"] == "checkout.session.completed":
        # retrieve the session data
        session = event['data']['object']

        # do whatever I want with the session
        handle_payment(session)

    # status 200 means everything's ok
    return HttpResponse(status=200)


@login_required
def handle_payment(session):
    user = get_object_or_404(User, pk=session["client_reference_id"])
    all_program_ids = session['metadata']['all_programs_id'].split(",")

    for program_id in all_program_ids:
        program_model = get_object_or_404(Program, pk=program_id)

        # create the purchase model
        purchase = Purchase()
        purchase.program_id = program_model
        purchase.user_id = user
        purchase.save()
