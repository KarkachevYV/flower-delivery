# admin_panel/urls.py
from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('manage-users/', views.manage_users, name='manage_users'),  # управление пользователями
    path('manage-orders/', views.manage_orders, name='manage_orders'),  # управление заказами
    path('manage-products/', views.manage_products, name='manage_products'),  # управление товарами
]
