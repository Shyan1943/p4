from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from dgs.models import Dg
from dgs.forms import DgForm
from .forms import SearchForm

# Create your views here.
# def index(request):
#     return HttpResponse("Welcome to home")
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

        return render(request, 'home/home.template.html', {
            "form": form,
            "dgs": dgs
        })
    else:
        dgs = Dg.objects.all()
        return render(request, 'home/home.template.html', {
            "form": form,
            "dgs": dgs
        })
