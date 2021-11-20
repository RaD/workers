from django.urls import path

from . import views

urlpatterns = [
    path('<forum_pk>/', views.forum_view, name='forum'),
    path('<forum_pk>/add/', views.post_add_view, name='post_add'),
    path('post/<post_pk>/', views.post_view, name='post'),
    path('post/<post_pk>/add/', views.reply_add_view, name='reply_add'),
    path('', views.index_view, name='index'),
    ]
