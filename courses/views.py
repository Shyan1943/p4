from django.shortcuts import HttpResponse


# Create your views here.
def all_courses(request):
    return HttpResponse("All courses")
