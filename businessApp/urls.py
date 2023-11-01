from django.urls import path
from businessApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_page', views.login_page, name='login_page'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
]
