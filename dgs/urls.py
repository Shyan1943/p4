from django.contrib import admin
from django.urls import path
import dgs.views

urlpatterns = [
    path('', dgs.views.index, name="show_dg_route"),
    path('create', dgs.views.create_dg, name="create_dg_route"),
    path('update/<dg_id>', dgs.views.update_dg, name="update_dg_route"),
    path('delete/<dg_id>', dgs.views.delete_dg, name="delete_dg_route")
]