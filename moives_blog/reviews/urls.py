from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('review_list/', views.reviews_list, name='review_list'),
    path('review_create/', views.review_create, name='review_create'),
    path('review_detail<int:pk>', views.review_detail, name='review_detail'),
    path('review_update<int:pk>', views.review_update, name='review_update'),
    path('review_delete<int:pk>', views.review_delete, name='review_delete'),
    path('create_comment/<int:pk>', views.create_comment, name='review_create_comment'),
    path('<int:review_id>/comments/<int:comment_id>/delete/', views.delete_comment, name='review_delete_comment')
]