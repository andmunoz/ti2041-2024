from ninja import NinjaAPI, Schema
from .models import Post
from django.http import Http404
from django.shortcuts import get_object_or_404
from pydantic import ValidationError

# Crea la API
api = NinjaAPI(
    title="API del Blog del Profe",
    description="Aquí están todos los servicios del profe",
    version="1.0.0"
)

# Manejadores de Errores
@api.exception_handler(Http404)
def error_404(request, ex):
    return api.create_response(request, 
                               {'response': 'Recurso no encontrado'},
                               status=404)
    
@api.exception_handler(ValidationError)
def error_validacion(request, ex):
    return api.create_response(request,
                               {
                                   'response': 'Error de Formato de Entrada',
                                   'errores': ex.errors()
                               },
                               status=422)

# Servicios de la API
# @api.get(path="posts/", tags=["Posts"])   
@api.api_operation(
    path="posts/",
    methods=["GET"],
    summary="Lista de Artículos",
    description="Se obtienen todos los artículos en orden de publicación",
    tags=["Posts"]
)
def get_posts(request):
    all_posts = Post.objects.all().order_by('publish_date').values()
    return list(all_posts)

@api.get(path="posts/{post_id}", tags=["Posts"])
def get_post(request, post_id: int):
    all_posts = Post.objects.filter(id=post_id).values()
    return list(all_posts)

class PostSchema(Schema):
    title: str
    text: str
    author_id: int
    category_id: int
    publish_date: str

@api.post(path="posts/", tags=["Posts"])
def add_post(request, data: PostSchema):
    post = Post.objects.create(**data.dict())
    return { "id":post.id, "title":post.title }

@api.put(path="posts/{post_id}", tags=["Posts"])
def update_post(request, post_id: int, data: PostSchema):
    post = get_object_or_404(Post, id=post_id)
    for attr, value in data.dict().items():
        setattr(post, attr, value)
    post.save()
    return { "id":post.id, "title":post.title }
