from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserCreateForm, UserEditForm

def list_users(request):
    usuarios = User.objects.all()
    return render(request, "users/list_users.html", {"usuarios": usuarios})

def create_user(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("list_users")
    else:
        form = UserCreateForm()
    return render(request, "users/create_user.html", {"form": form})


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("list_users")
    else:
        form = UserEditForm(instance=user)
    return render(request, "users/edit_user.html", {"form": form, "user": user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("list_users")
    return render(request, "users/delete_user.html", {"user": user})
