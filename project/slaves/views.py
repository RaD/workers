from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from project.slaves.forms import ResumeForm
from project.slaves.models import Resume


def index_view(request):
    """Вьюха отображает главную страницу приложения"""
    qs = Resume.objects.all()
    context = {
        'queryset': qs,
        }
    return render(request, 'slaves/index.html', context)


def creates_view(request):
    """ Показывает или обрабатывает форму """
    form = ResumeForm(request.POST or None)
    context = {
        'form': form,
        }
    if request.method == 'POST' and form.is_valid():
        if request.user.is_anonymous:
            return HttpResponseForbidden('Не авторизован')
        form.save(request.user)
        return redirect('slaves:index')
    return render(request, 'slaves/create.html', context)
