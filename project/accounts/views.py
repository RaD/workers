from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, TemplateView

from project.accounts import forms


class RegisterView(FormView):
    template_name = 'registration/register_form.html'
    form_class = forms.RegisterForm
    from_email = 'support@project.ru'
    subject_template = 'registration/email_subject.txt'
    email_template_name = ''
    html_email_template_name = None
    success_url = reverse_lazy('accounts:register_done')
    title = 'Сброс пароля'
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form()
            if form.is_valid():
                form.save()
        return super().dispatch(request, *args, **kwargs)


class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'
