from django.shortcuts import render, redirect
from models import Mascota

# Create your views here.
def index(request):
    todos = Mascota.objects.all().order_by('nombre')

    context = {
        todos: todos, 
    }

    return render(request, 'mascotas.html', context)
