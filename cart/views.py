from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from programs.models import Program


# Create your views here.
def add_to_cart(request, program_id):
    print(program_id)
    return HttpResponse("Pro added")
