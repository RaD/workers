from django.shortcuts import render

from . import models


def index_view(request):
    """Вьюха отображает главную страницу приложения"""
    context = {
        'queryset': None,
        }
    return render(request, 'forum/index.html', context)
