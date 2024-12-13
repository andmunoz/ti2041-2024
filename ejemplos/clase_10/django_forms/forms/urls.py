from django.urls import path
from .views import list_users, create_user, edit_user, delete_user

urlpatterns = [
    path("", list_users, name="list_users"),
    path("create/", create_user, name="create_user"),
    path("edit/<int:user_id>/", edit_user, name="edit_user"),
    path("delete/<int:user_id>/", delete_user, name="delete_user"),
]