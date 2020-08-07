from django.shortcuts import HttpResponse, render, redirect, reverse
from django.contrib import messages
# from django.db.models import Q
from django.contrib.auth.decorators import login_required
# from .models import Program
from .forms import ProgramForm


# Create your views here.
def all_programs(request):
    return HttpResponse("all programs")


@ login_required
def create_program(request):
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            create_program = form.save(commit=False)
            create_program.user = request.user
            create_program.save()
            messages.success(request,
                             "New program has been created successfully")
            return redirect(reverse(all_programs))
        else:
            return render(request, 'programs/create_program.template.html', {
                'form': form
            })

    else:
        form = ProgramForm()
        return render(request, 'programs/create_program.template.html', {
            'form': form
        })
