from django.urls import path
from businessApp import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
]