from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login_page', views.login_page)
]