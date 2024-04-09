from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('main_page', views.main_page),
    path('create_movie', views.create_movie),
    path('detail_page', views.detail_page)
]