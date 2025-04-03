# accounts/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Используем стандартные LoginView и LogoutView
from .views import user_info
from . import views
from accounts.views import UserListView


app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('user_info/<int:user_id>/', user_info, name='user_info'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),  # Стандартный LoginView
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]

