from django.urls import path

from project.accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/done/', views.RegisterDoneView.as_view(), name='register_done'),
    ]
