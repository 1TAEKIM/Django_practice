from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('main_page/', views.main, name='main'),
    path('create_movie/', views.create_movie),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>',views.update, name='update')
]