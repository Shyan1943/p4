from django.contrib import admin
from django.urls import path
import programs.views

urlpatterns = [
    path('', programs.views.all_programs),
]