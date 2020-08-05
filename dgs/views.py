from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Dg
from .forms import DgForm


# Create your views here.
def index(request):
    dgs = Dg.objects.all()
    return render(request, "dgs/dg.template.html", {
        "dgs": dgs
    })

@login_required
def create_dg(request):
    if request.method == "POST":
        create_form = DgForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            return render(request, "dgs/create_dg.template.html", {
                "form": create_form
            })
    else:
        create_form = DgForm()
        return render(request, "dgs/create_dg.template.html", {
                "form": create_form
        })

@login_required
def update_dg(request, dg_id):
    dg_being_updated = get_object_or_404(Dg, pk=dg_id)
    if request.method == "POST":
        dg_form = DgForm(request.POST, instance=dg_being_updated)
        if dg_form.is_valid:
            dg_form.save()
            return redirect(reverse(index))
        else:
            return render(request, "dgs/update_dg.template.html", {
                "form": dg_form
            })
    else:
        dg_form = DgForm(instance=dg_being_updated)
        return render(request, "dgs/update_dg.template.html", {
            "form": dg_form
        })

@login_required
def delete_dg(request, dg_id):
    dg_to_delete = get_object_or_404(Dg, pk=dg_id)
    if request.method == "POST":
        dg_to_delete.delete()
        return redirect(index)
    else:
        return render(request, "dgs/delete_dg.template.html", {
            "dg": dg_to_delete
        })
