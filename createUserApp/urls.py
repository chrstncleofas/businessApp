from django.urls import path
from . import views

urlpatterns = [
    path('', views.createUserPage, name='createUserPage'),
]
