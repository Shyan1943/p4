from django.contrib import admin
from django.urls import path
import reviews.views

urlpatterns = [
    path('', reviews.views.reviews),
    path('create/<dg_id>', reviews.views.create_review,
         name='create_review_route'),
    path('create/comment/<review_id>', reviews.views.create_comment,
         name='create_comment_route')
]