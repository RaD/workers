from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import models
from . import forms


def index_view(request):
    """Вьюха отображает главную страницу приложения"""
    qs = models.Group.objects.all()
    context = {
        'queryset': qs,
        }
    return render(request, 'forum/index.html', context)


def forum_view(request, forum_pk):
    """Отображаем содержимое указанного форума"""
    forum = models.Forum.objects.get(pk=forum_pk)
    context = {
        'forum': forum,
        }
    return render(request, 'forum/forum.html', context)


def post_view(request, post_pk):
    """Отображаем содержимое поста"""
    post = models.Post.objects.get(pk=post_pk)
    context = {
        'post': post,
        }
    return render(request, 'forum/post.html', context)


@login_required
def post_add_view(request, forum_pk):
    form = forms.PostForm(request.POST or None)
    forum = models.Forum.objects.get(pk=forum_pk)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(request.user, forum)
            return redirect(obj)
    context = {'form': form, 'forum': forum, 'about': 'Новый пост'}
    return render(request, 'forum/form.html', context)


@login_required
def reply_add_view(request, post_pk):
    form = forms.ReplyForm(request.POST or None)
    post = models.Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(request.user, post)
            return redirect(obj)
    context = {'form': form, 'forum': post.forum, 'post': post,
               'about': f'Новый отклик на "{post.text}"'}
    return render(request, 'forum/form.html', context)
