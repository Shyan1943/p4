from django.shortcuts import render, HttpResponse
from .models import Dg


# Create your views here.
def index(request):
    dgs = Dg.objects.all()
    return render(request, "dgs/dg.template.html", {
        "dgs": dgs
    })