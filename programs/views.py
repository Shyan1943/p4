from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Program
from .forms import ProgramForm


# Create your views here.
def all_programs(request):
    programs = Program.objects.all()
    return render(request, "programs/all_programs.template.html", {
        "programs": programs
    })


@login_required
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


@login_required
def update_program(request, program_id):
    if request.user.groups.filter(name='customer').exists():
        messages.error(request, "You are not a Site administrator")
        return redirect(reverse(all_programs))

    program_being_updated = get_object_or_404(Program, pk=program_id)
    if request.method == "POST":
        program_form = ProgramForm(request.POST,
                                   instance=program_being_updated)
        if program_form.is_valid:
            program_form.save()
            messages.success(
                request,
                f'Post "{program_being_updated.title}" has been updated')
            return redirect(reverse(all_programs))
        else:
            return render(request, "programs/update_program.template.html", {
                "form": program_form,
                "program": program_being_updated
            })
    else:
        program_form = ProgramForm(instance=program_being_updated)
        return render(request, "programs/update_program.template.html", {
            "form": program_form,
            "program": program_being_updated
        })
