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
    programs = Program.objects.all()

    if request.GET:
        # create a query that is always true
        query = ~Q(pk__in=[])

        # if the user fills in any keyword and its not an empty string
        if "anykeyword" in request.GET and request.GET["anykeyword"]:
            anykeyword = request.GET["anykeyword"]
            query = query & Q(topic__icontains=anykeyword) | Q(
                description__icontains=anykeyword)

        if "imdg_code" in request.GET and request.GET["imdg_code"]:
            imdg_code_id = request.GET['imdg_code']
            query = query & Q(imdg_code=imdg_code_id)

        # to reassign back to the query set
        dgs = dgs.filter(query)

        # create a query that is always true
        query = ~Q(pk__in=[])

        # if the user fills in any keyword and its not an empty string
        if "anykeyword" in request.GET and request.GET["anykeyword"]:
            anykeyword = request.GET["anykeyword"]
            query = query & Q(title__icontains=anykeyword) | Q(
                who_should_attend__icontains=anykeyword) | Q(
                outline__icontains=anykeyword) | Q(
                objectives__icontains=anykeyword) | Q(
                accreditation_and_examination__icontains=anykeyword) | Q(
                fees__icontains=anykeyword)

        # to reassign back to the query set
        programs = programs.filter(query)

        return render(request, 'home/home.template.html', {
            "form": form,
            "dgs": dgs,
            "programs": programs
        })
    else:
        # if the user never submit form, then just display all Dgs & Programs
        return render(request, 'home/home.template.html', {
            "form": form,
            "dgs": dgs,
            "programs": programs
        })
