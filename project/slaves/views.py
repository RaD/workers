from django.http import HttpResponse
from django.shortcuts import render

from project.slaves.models import Resume
from project.slaves.forms import ResumeForms


def index_view(request):
    """Вьюха отображает главную страницу приложения"""
    qs = Resume.objects.all()
    form = ResumeForms(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        return HttpResponse('oK')
    else:
        context = {
            'title': 'Рабы на галерах',
            'queryset': qs,
            'form': form,
            }
    return render(request, 'slaves/index.html', context)
