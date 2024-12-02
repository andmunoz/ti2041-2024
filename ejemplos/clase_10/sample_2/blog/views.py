from django.shortcuts import render, redirect, HttpResponse
from .forms import PostForm
from .models import Post, Tag, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required, login_required


# Vistas para autenticar y desconectar al usuario
def log_in(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        clave = request.POST['clave']
        user = authenticate(request, username=usuario, password=clave)
        
        if user is None:
            return HttpResponse('Error de autenticación', status=401)

        login(request, user=user)
        return redirect('/')
         
    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('/')


# Vista de inicio que muestra la lista de artículos
def index(request):
    all_posts = Post.objects.all().order_by('publish_date')
    
    actual_posts = []
    for post in all_posts:
        tags = post.tags.all()
        actual_post = {
            'id': post.id,
            'title': post.title,
            'author': post.author,
            'category': post.category,
            'tags': tags,
            'publish_date': post.publish_date,
        }
        actual_posts.append(actual_post)
    
    context = { 
        'user_authenticated': request.user.is_authenticated, 
        'posts': actual_posts 
    }
    return render(request, 'index.html', context)


# Vista de detalle de un artículo
def details(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(id=post_id)
    tags = Post.tags.all()
    context = { 
        'post': post,
        'tags': tags 
    }
    return render(request, 'details.html', context)


# Vista para crear un artículo (debe estar autenticado)
@login_required(login_url='/login')
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.author = request.user
            post.save()
            tag_list = request.POST.getlist('tags', [])
            post.tags.set(tag_list)
            return redirect('/')
        else:
            print('Error en el Formulario')
            print(form.errors)
    
    categories = Category.objects.all().order_by('description')
    tags = Tag.objects.all().order_by('description')
    form = PostForm()
    context = {
        'categories': categories,
        'tags': tags,
        'form': form
    }
    return render(request, 'new.html', context)