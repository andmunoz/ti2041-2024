from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("details/", views.details),
    path("login/", views.login),
    path("accounts/login/", views.login),
    path("logout/", views.desconectarse),
    path("new/", views.new_form),
]