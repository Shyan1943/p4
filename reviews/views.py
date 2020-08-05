from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm


# Create your views here.
def reviews(request):
    return HttpResponse("All Reviews")


@login_required
def create_review(request):
    if request.method == "POST":
        create_form = ReviewForm(request.POST)
        if create_form.is_valid():
            create_review = create_form.save(commit=False)
            create_review.user = request.user
            create_review.save()
            messages.success(request,
                             "New review has been created successfully!!")
            return redirect(reverse(reviews))
        else:
            return render(request, "reviews/create_review.template.html", {
                "form": create_form
            })
    else:
        create_form = ReviewForm()
        return render(request, "reviews/create_review.template.html", {
            "form": create_form
        })
