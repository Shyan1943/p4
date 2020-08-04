from django.contrib import admin
from django.urls import path, include
import dgs.views

urlpatterns = [
    path('', dgs.views.index),
]