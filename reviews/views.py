from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dgs.models import Dg
from .models import Review
from .forms import ReviewForm, CommentForm


# Create your views here.
def reviews(request):
    return HttpResponse("All Reviews")


@login_required
def create_review(request, dg_id):
    dg = get_object_or_404(Dg, pk=dg_id)
    if request.method == "POST":
        create_form = ReviewForm(request.POST)
        if create_form.is_valid():
            create_review = create_form.save(commit=False)
            create_review.user = request.user
            create_review.dg = dg
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
            "form": create_form,
            "dg": dg
        })


@login_required
def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            messages.success(request,
                             "New comment has been created successfully!!")
            return redirect(reverse(reviews))
        else:
            return render(request, "reviews/create_comment.template.html", {
                "form": form
            })
    else:
        form = CommentForm()
        return render(request, "reviews/create_comment.template.html", {
            "form": form,
            "review": review
        })
