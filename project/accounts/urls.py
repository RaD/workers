from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from project.accounts import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/done/', views.RegisterDoneView.as_view(), name='register_done'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    ]
