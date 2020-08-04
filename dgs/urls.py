from django.contrib import admin
from django.urls import path
import dgs.views

urlpatterns = [
    path('', dgs.views.index),
    path('create', dgs.views.create_dg, name="create_dg_route"),
    path('update/<dg_id>', dgs.views.update_dg, name="update_dg_route")
]