from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Program
from .forms import ProgramForm


# Create your views here.
def all_programs(request):
    programs = Program.objects.all()
    return render(request, "programs/all_programs.template.html", {
        "programs": programs
    })


def create_program(request):
    if request.user.groups.filter(name='customer').exists():
        messages.error(request, "You are not a Site administrator")
        return redirect(reverse(all_programs))

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
