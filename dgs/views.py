from django.shortcuts import render, redirect, reverse
from .models import Dg
from .forms import DgForm


# Create your views here.
def index(request):
    dgs = Dg.objects.all()
    return render(request, "dgs/dg.template.html", {
        "dgs": dgs
    })


def create_dg(request):
    if request.method == "POST":
        create_form = DgForm(request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect(reverse(index))
        else:
            return render(request, 'dgs/create_dg.template.html', {
                'form': create_form
            })
    else:
        create_form = DgForm()
        return render(request, 'dgs/create_dg.template.html', {
                'form': create_form
        })
