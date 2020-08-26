from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from dgs.models import Dg
from programs.models import Program
from .forms import SearchForm


# Create your views here.
# Landing Page

# ALL view functions must take in the variable request as the first argumernt

# When Users who direct to a non-existent page or resource...
def error_404_view(request, exception):
    # Error notification message given
    messages.error(
        request, "Sorry, The page is missing or does not exist. You are"
        " redirecting back to the homepage")

    # and users are redirected back to the main page without having to use the
    # browser navigation buttons
    return render(request, "home/home.template.html")


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
