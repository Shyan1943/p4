from django.shortcuts import render
from django.db.models import Q
from dgs.models import Dg
from programs.models import Program
from .forms import SearchForm


# Create your views here.
# Landing Page

# ALL view functions must take in the variable request as the first argumernt
def index(request):
    form = SearchForm(request.GET)

    # select all from Dgs & Promgrams
    dgs = Dg.objects.all()
    # programs = Program.objects.all()

    if request.GET:
        # create a query that is always true
        query = ~Q(pk__in=[])

        # if the user fills in the title and the title is not an empty string
        if "title" in request.GET and request.GET["title"]:
            title = request.GET["title"]
            query = query & Q(title__icontains=title)|Q(example__icontains=title)

        if "imdg_code" in request.GET and request.GET["imdg_code"]:
            imdg_code_id = request.GET['imdg_code']
            query = query & Q(imdg_code=imdg_code_id)

        # to reassign back to the query set
        dgs = dgs.filter(query)
        # programs = programs.filter(query)

        return render(request, 'home/home.template.html', {
            "form": form,
            "dgs": dgs,
            # "programs": programs
        })
    else:
        # if the user never submit form, then just display all Dgs & Programs
        return render(request, 'home/home.template.html', {
            "form": form,
            "dgs": dgs,
            # "programs": programs
        })
