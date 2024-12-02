from django.urls import path
from . import views
from .api import api

urlpatterns = [
    path("", views.index),
    path("details/", views.details),
    path("login/", views.log_in),
    path("accounts/login/", views.log_in),
    path("logout/", views.log_out),
    path("new/", views.new_post),
    path("api/", api.urls)
]