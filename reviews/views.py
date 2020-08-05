from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import messages
from .forms import ReviewForm


# Create your views here.
def reviews(request):
    return HttpResponse("All Reviews")


def create_review(request):
    if request.method == "POST":
        create_form = ReviewForm(request.POST)
        if create_form.is_valid():
            create_form.save()
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
