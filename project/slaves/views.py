from django.shortcuts import render

from project.slaves.models import Resume


def index_view(request):
    """Вьюха отображает главную страницу приложения"""
    qs = Resume.objects.all()
    context = {
        'title': 'Рабы на галерах',
        'queryset': qs,
        }
    return render(request, 'slaves/index.html', context)
