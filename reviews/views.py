from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dgs.models import Dg
from .models import Review
from .forms import ReviewForm, CommentForm


# Create your views here.
# A view (in other words, a view function) refers to a function
# that is called when its corrosponding URL is visited in the browser


# ALL view functions must take in the variable request as the first argumernt
def reviews(request):
    return HttpResponse("All Reviews")


@login_required
def create_review(request, dg_id):
    # retrieve the DG that we want to create review
    dg = get_object_or_404(Dg, pk=dg_id)

    # check if we are submitting the form
    if request.method == "POST":

        # create the ReviewForm by filling it with data from the user's
        # submission
        create_form = ReviewForm(request.POST)
        if create_form.is_valid():
            create_review = create_form.save(commit=False)
            create_review.user = request.user
            create_review.dg = dg

            # create a model based on the data in the form
            create_review.save()

            # message prompt when the review is created
            messages.success(request,
                             "New review has been created successfully!!")

            # redirect back to the DG details review page function
            return redirect(reverse(reviews))
        else:
            return render(request, "reviews/create_review.template.html", {
                "form": create_form
            })
    else:
        # create an instance of the class ReviewForm and store it in the form
        # variable
        create_form = ReviewForm()
        return render(request, "reviews/create_review.template.html", {
            "form": create_form,
            "dg": dg
        })


@login_required
def create_comment(request, review_id):
    # retrieve the review that we want to create comment
    review = get_object_or_404(Review, pk=review_id)

    # check if we are submitting the form
    if request.method == "POST":

        # create the CommentForm by filling it with data from the user's
        # submission
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user

            # create a model based on the data in the form
            comment.save()

            # message prompt when the comment is created
            messages.success(request,
                             "New comment has been created successfully!!")

            # redirect back to the DG details page function
            return redirect(reverse(reviews))
        else:
            return render(request, "reviews/create_comment.template.html", {
                "form": form
            })
    else:
        # create an instance of the class CommentForm and store it in the form
        # variable
        form = CommentForm()
        return render(request, "reviews/create_comment.template.html", {
            "form": form,
            "review": review
        })

