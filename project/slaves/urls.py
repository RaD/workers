from django.urls import re_path

from project.slaves import views

urlpatterns = [
    re_path('^$', views.index_view, name='index'),
    re_path('^create/$', views.creates_view, name='create'),
    ]
