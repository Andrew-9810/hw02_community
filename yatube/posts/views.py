from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from users.views import authorized_only
# from django.contrib.auth.decorators import login_required
SHOW_QUANTITY: int = 10


def index(request):
    """Главная страница."""
    template = 'posts/index.html'
    posts = Post.objects.order_by()[:SHOW_QUANTITY]
    context = {
        'posts': posts
    }
    return render(request, template, context)

# @login_required


@authorized_only
def group_posts(request, slug):
    """Страница постов отсортированных по группам."""
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = (group.posts_group.all()[:SHOW_QUANTITY])
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
