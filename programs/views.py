from django.shortcuts import HttpResponse


# Create your views here.
def all_programs(request):
    return HttpResponse("all programs")
