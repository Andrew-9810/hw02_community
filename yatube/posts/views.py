from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    """Главная страница"""
    SHOW_QUANTITY: int = 10
    template = 'posts/index.html'
    posts = Post.objects.order_by()[:SHOW_QUANTITY]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Страница постов отсортированных по группам"""
    SHOW_QUANTITY: int = 10
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = (
        group.posts_group.all()[:SHOW_QUANTITY]
    )
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)

# Create your views here.
