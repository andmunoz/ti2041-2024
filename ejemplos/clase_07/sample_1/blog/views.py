from django.shortcuts import render, redirect
from .models import Post, Tag, Category


from django.contrib.auth.models import User

def create_user(request):
    user = User.objects.create_user(
            username = request.POST.get('username'),
            password = request.POST.get('password'),
            email = request.POST.get('email')
        )


from django.contrib.auth import authenticate, login

def iniciar_sesion(request):
    username = request.POST['username']
    password = request.POST['password']
    
    # Verifica las credenciales
    usuario = authenticate(request, username=username, password=password)
    
    if usuario is not None:
        # Inicia la sesión del usuario
        login(request, usuario)
        return redirect('home')
    else:
        # Maneja error de autenticación
        return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    

from django.contrib.auth import logout

def cerrar_sesion(request):
    logout(request)
    return redirect('login')


def index(request):
    all_posts = Post.objects.all().order_by('publish_date')
    
    actual_posts = []
    for post in all_posts:
        tags = Tag.objects.filter(post__id = post.id)
        actual_post = {
            'id': post.id,
            'title': post.title,
            'author': post.author,
            'category': post.category,
            'tags': tags,
            'publish_date': post.publish_date,
        }
        actual_posts.append(actual_post)
    
    context = { 'posts': actual_posts }
    return render(request, 'index.html', context)


def details(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(id = post_id)
    tags = Tag.objects.filter(post__id = post_id)
    context = { 
                'post': post,
                'tags': tags 
              }
    return render(request, 'details.html', context)


def session_example(request):

    # Get a session object from request
    session = request.session

    # Put a new value in active session
    session['key'] = 'value'

    # Get a value from active session
    value = session.get('key', 'default_value')


from django.contrib.auth.decorators import login_required

@login_required
def acceso_atenticado(request):
    return render(request, 'protegida.html')


from django.contrib.auth.decorators import permission_required

@permission_required('app_name.can_edit', raise_exception=True)
def vista_editar(request):
    # Código de la vista
    pass

