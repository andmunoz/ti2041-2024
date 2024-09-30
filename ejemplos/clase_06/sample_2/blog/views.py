from django.shortcuts import render
from .models import Post, Tag, Category

# Create your views here.
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