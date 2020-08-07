from django.contrib import admin
from django.urls import path
import courses.views

urlpatterns = [
    path("", courses.views.all_courses),
]
