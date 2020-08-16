from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Dg
from .forms import DgForm


# Create your views here.
def all_dg(request):

    # SELECT * FROM Dgs
    dgs = Dg.objects.all()
    return render(request, "dgs/dg.template.html", {
        "dgs": dgs
    })


# View a dg details
def view_dg(request, dg_id):
    dg_being_view = get_object_or_404(Dg, pk=dg_id)
    return render(request, "dgs/details_dg.template.html", {
        "dg": dg_being_view
    })


@login_required
def create_dg(request):

    # check if we are submitting the form
    if request.method == "POST":

        # create the BooKForm by filling it with data from the user's
        # submission
        create_form = DgForm(request.POST)

        if create_form.is_valid():
            create_dg = create_form.save(commit=False)
            create_dg.user = request.user

            # create a model based on the data in the form
            create_dg.save()

            # message prompt out when Dg is created
            messages.success(request, "New post has been created")

            # redirect back to the all_dg view function
            return redirect(reverse(all_dg))
        else:
            return render(request, "dgs/create_dg.template.html", {
                "form": create_form
            })
    else:
        # create an instance of the class DgForm and store it in the form
        # variable
        create_form = DgForm()
        return render(request, "dgs/create_dg.template.html", {
                "form": create_form
        })


@login_required
def update_dg(request, dg_id):
    # retrieve the dg which we going to update
    dg_being_updated = get_object_or_404(Dg, pk=dg_id)

    # if the user has submitted the form
    if request.method == "POST":
        dg_form = DgForm(request.POST, instance=dg_being_updated)
        if dg_form.is_valid():
            dg_form.save()
            messages.success(
                request,
                f'Post "{dg_being_updated.title}" has been updated')
            return redirect(reverse(all_dg))
        else:
            # if the user didn't submit the form
            return render(request, "dgs/update_dg.template.html", {
                "form": dg_form,
                "dg": dg_being_updated
            })
    # or to show it in a form
    else:
        dg_form = DgForm(instance=dg_being_updated)
        return render(request, "dgs/update_dg.template.html", {
            "form": dg_form,
            "dg": dg_being_updated
        })


@login_required
def delete_dg(request, dg_id):
    # retrieve the dg which we going to delete
    dg_to_delete = get_object_or_404(Dg, pk=dg_id)

    # if the form is submitted
    if request.method == "POST":
        dg_to_delete.delete()
        messages.success(
                request,
                f'Post "{dg_to_delete.title}" has been deleted')
        return redirect(reverse(all_dg))
    else:
        # if no form is submitted (that is, just to see the confirmation
        return render(request, "dgs/delete_dg.template.html", {
            "dg": dg_to_delete
        })
