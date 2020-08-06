from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Dg
from .forms import DgForm, SearchForm


# Create your views here.
def index(request):
    form = SearchForm(request.GET)

    if request.GET:
        query = ~Q(pk__in=[])

        if "title" in request.GET and request.GET["title"]:
            title = request.GET["title"]
            query = query & Q(title__icontains=title)

        if "imdg_code" in request.GET and request.GET["imdg_code"]:
            imdg_code_id = request.GET['imdg_code']
            query = query & Q(imdg_code=imdg_code_id)

        dgs = Dg.objects.all()
        dgs = dgs.filter(query)

        return render(request, 'dgs/home.template.html', {
            "form": form,
            "dgs": dgs
        })
    else:
        dgs = Dg.objects.all()
        return render(request, 'dgs/home.template.html', {
            "form": form,
            "dgs": dgs
        })


def all_dg(request):
    dgs = Dg.objects.all()
    return render(request, "dgs/dg.template.html", {
        "dgs": dgs
    })


def view_dg(request, dg_id):
    dg_being_view = get_object_or_404(Dg, pk=dg_id)
    return render(request, "dgs/details_dg.template.html", {
        "dg": dg_being_view
    })


@login_required
def create_dg(request):
    if request.method == "POST":
        create_form = DgForm(request.POST)

        if create_form.is_valid():
            create_dg = create_form.save(commit=False)
            create_dg.user = request.user
            create_dg.save()
            messages.success(request, "New post has been created")
            return redirect(reverse(all_dg))
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
            messages.success(
                request,
                f'Post "{dg_being_updated.title}" has been updated')
            return redirect(reverse(all_dg))
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
        messages.success(
                request,
                f'Post "{dg_to_delete.title}" has been deleted')
        return redirect(index)
    else:
        return render(request, "dgs/delete_dg.template.html", {
            "dg": dg_to_delete
        })
