from django.urls import path
import programs.views

urlpatterns = [
    path('', programs.views.all_programs, name="all_programs_route"),
    path('create/', programs.views.create_program,
         name="create_program_route"),
    path('update/<program_id>', programs.views.update_program,
         name="update_program_route"),
    path('delete/<program_id>', programs.views.delete_program,
         name="delete_program_route")
]
