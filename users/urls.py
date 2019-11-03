"""Defines URL patterns  in the users section"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    # The Login Page
    path('login/', LoginView.as_view(template_name='users/login.html'),
              name="login"),

    # The Logout Page
    path('logout/', views.logout_view, name='logout'),

    # The Registration Page
    path('register/', views.register, name='register'),


]


