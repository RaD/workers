from django.conf import settings


def common_vars(request):
    return {
        'settings': settings,
        }
