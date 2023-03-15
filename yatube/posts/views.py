from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from users.views import authorized_only
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

User = get_user_model()
SHOW_QUANTITY: int = 10


def index(request):
    """Главная страница."""
    template = 'posts/index.html'
    posts = Post.objects.order_by()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


@authorized_only
def group_posts(request, slug):
    """Страница постов отсортированных по группам."""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = (group.posts_group.all())
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    """Запрос к модели и создание словаря контекста"""
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    count_post = posts.count()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template = 'posts/profile.html'
    context = {
        'username': author,
        'page_obj': page_obj,
        'count': count_post,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    """Страница просмотра отдельного поста"""
    post = get_object_or_404(Post, id=post_id)
    if post.group_id is None:
        group = ""
    else:
        group = Group.objects.get(id=post.group_id)
    author = User.objects.get(id=post.author_id)
    count_post = Post.objects.filter(author_id=post.author_id).count()
    template = 'posts/post_detail.html'
    context = {
        'post': post,
        'group': group,
        'author': author,
        'count': count_post
    }
    return render(request, template, context)
