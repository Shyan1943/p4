from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Program
from .forms import ProgramForm


# Create your views here.
def all_programs(request):
    # SELECT * FROM Programs
    programs = Program.objects.all()
    return render(request, "programs/all_programs.template.html", {
        "programs": programs
    })


# View a Program details
def view_program(request, program_id):
    program_being_view = get_object_or_404(Program, pk=program_id)
    return render(request, "programs/details_program.template.html", {
        "p": program_being_view
    })


@login_required
def create_program(request):
    if request.user.groups.filter(name='customer').exists():
        messages.error(request, "You are not a Site administrator")
        return redirect(reverse(all_programs))

    # check if we are submitting the form
    if request.method == "POST":

        # create the ProgramForm by filling it with data from the user's
        form = ProgramForm(request.POST)
        if form.is_valid():
            create_program = form.save(commit=False)
            create_program.user = request.user

            # create a model based on the data in the form
            create_program.save()

            # message prompt out when the Dg is created
            messages.success(request,
                             "New program has been created successfully")

            # redirect back to the all_programs view function
            return redirect(reverse(all_programs))
        else:
            return render(request, 'programs/create_program.template.html', {
                'form': form
            })

    else:
        # create an instance of the class ProgramForm and store it in the form
        # variable
        form = ProgramForm()
        return render(request, 'programs/create_program.template.html', {
            'form': form
        })


@login_required
def update_program(request, program_id):
    if request.user.groups.filter(name='customer').exists():
        messages.error(request, "You are not a Site administrator")
        return redirect(reverse(all_programs))

    # retrieve the program that we want to edit
    program_being_updated = get_object_or_404(Program, pk=program_id)

    # check if we are submitting the form
    if request.method == "POST":

        # the user has submitted data by extracting it from the request.POST
        # and passing it to the form
        program_form = ProgramForm(request.POST,
                                   instance=program_being_updated)
        if program_form.is_valid:

            # create a model based on the data in the form
            program_form.save()

            # message prompt out when the Dg is updated
            messages.success(
                request,
                f'Post "{program_being_updated.title}" has been updated')

            # redirect back to the all_programs view function
            return redirect(reverse(all_programs))
        else:
            return render(request, "programs/update_program.template.html", {
                "form": program_form,
                "program": program_being_updated
            })
    else:
        # if there is no form submitted, then we display the form
        # populate the form with the existing data from the program
        program_form = ProgramForm(instance=program_being_updated)
        return render(request, "programs/update_program.template.html", {
            "form": program_form,
            "program": program_being_updated
        })


@login_required
def delete_program(request, program_id):
    if request.user.groups.filter(name='customer').exists():
        messages.error(request, "You are not a Site administrator")
        return redirect(reverse(all_programs))

    # retrieve the book that we want to delete
    program_to_delete = get_object_or_404(Program, pk=program_id)

    # check if we are submitting the form
    if request.method == "POST":
        program_to_delete.delete()

        # message prompt out when the Dg is deleted
        messages.success(
                request,
                f'Post "{program_to_delete.title}" has been deleted')

        # redirect back to the all_programs view function
        return redirect(reverse(all_programs))
    else:
        # if no form is submitted (that is, just to see the confirmation)
        return render(request, "programs/delete_program.template.html", {
            "program": program_to_delete
        })
