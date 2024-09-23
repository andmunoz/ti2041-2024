from django.shortcuts import render, redirect
from models import Perro

# Create your views here.
def index(request):
    todos = Perro.objects.all().order_by('nombre')
    poodles = Perro.objects.filter(raza='Poodle').order_by('nombre')
    hembras = Perro.objects.filter(genero='H').order_by('nombre')

    context = {
        todos: todos, 
        poodles: poodles,
        hembras: hembras
    }

    return render(request, 'perros.html', context)


def create(request):
    perro = Perro(
        name = 'Bobbie',
        raza = 'Poodle',
        edad = 7,
        genero = 'M'
    )
    perro.save()

    return redirect('index')


def update(request):
    perro = Perro.objects.get(id=1)
    perro.edad = 8
    perro.save()

    return redirect('index')
