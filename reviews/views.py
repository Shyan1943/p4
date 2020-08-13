from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dgs.models import Dg
from .models import Review
from .forms import ReviewForm


# Create your views here.
# A view (in other words, a view function) refers to a function
# that is called when its corrosponding URL is visited in the browser
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

            # redirect back to that DG details page function
            return render(request, "dgs/details_dg.template.html", {
                "dg": dg
            })
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
def update_review(request, dg_id, review_id):
    # retrieve the data that we want to update review
    review_being_updated = get_object_or_404(Review, pk=review_id)
    dg_being_view = get_object_or_404(Dg, pk=dg_id)

    # if the user has submitted the form, process the update
    if request.method == "POST":

        # the user has submitted data by extracting it from the request.POST
        # and passing it to the form
        review_form = ReviewForm(request.POST,
                                 instance=review_being_updated)
        if review_form.is_valid:
            review_form.save()
            messages.success(
                request,
                f'Post "{review_being_updated.title}" has been updated')
            # return back to that particular DG details page
            return render(request, "dgs/details_dg.template.html", {
                "dg": dg_being_view
            })
        else:
            # if the form submitted is invalid, then we display the form
            return render(request, "reviews/update_review.template.html", {
                "form": review_form,
                "review": review_being_updated
            })
    else:
        # if there is no form submitted, then we display the form

        # populate the form with the existing data from the review
        review_form = ReviewForm(instance=review_being_updated)
        return render(request, "reviews/update_review.template.html", {
            "form": review_form,
            "review": review_being_updated,
        })


@login_required
def delete_review(request, dg_id, review_id):
    # retrieve the data that we want to update review
    review = get_object_or_404(Review, pk=review_id)
    dg_being_view = get_object_or_404(Dg, pk=dg_id)

    # if the form is submitted
    if request.method == "POST":
        review.delete()
        # return back to that particular DG details page
        return render(request, "dgs/details_dg.template.html", {
            "dg": dg_being_view
        })
    else:
        # if no form is submitted (that is, just to see the confirmation)
        return render(request, 'reviews/delete_review.template.html', {
            'review': review
        })
