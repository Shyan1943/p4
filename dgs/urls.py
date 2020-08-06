from django.contrib import admin
from django.urls import path
import dgs.views

urlpatterns = [
    path('home', dgs.views.index, name="home"),
    path('', dgs.views.all_dg, name="show_dg_route"),
    path('create', dgs.views.create_dg, name="create_dg_route"),
    path('update/<dg_id>', dgs.views.update_dg, name="update_dg_route"),
    path('delete/<dg_id>', dgs.views.delete_dg, name="delete_dg_route"),
    path('details/<dg_id>', dgs.views.view_dg, name="view_dg_route")
]