from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('review_list/', views.reviews_list, name='review_list'),
    path('review_create/', views.review_create, name='review_create'),
    path('review_detail<int:pk>', views.review_detail, name='review_detail'),
    path('review_update<int:pk>', views.review_update, name='review_update')
]