from django.shortcuts import render, HttpResponse


# Create your views here.
def all_courses(request):
    return HttpResponse("All courses")
