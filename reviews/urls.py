from django.urls import path
import reviews.views

urlpatterns = [
    path('create/<dg_id>', reviews.views.create_review,
         name='create_review_route'),
    path('update/<dg_id>/<review_id>', reviews.views.update_review,
         name='update_review_route'),
    path('delete/<dg_id>/<review_id>', reviews.views.delete_review,
         name='delete_review_route')
]
