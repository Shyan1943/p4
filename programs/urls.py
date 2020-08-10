from django.contrib import admin
from django.urls import path
import programs.views

urlpatterns = [
    path('', programs.views.all_programs, name="all_programs_route"),
    path('create/', programs.views.create_program)
]