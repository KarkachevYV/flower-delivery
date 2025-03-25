# admin_panel/urls.py
from django.urls import path
from .views import dashboard, manage_users, manage_orders, manage_products


app_name = 'admin_panel'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('manage-users/', manage_users, name='manage_users'),  # управление пользователями
    path('manage-orders/', manage_orders, name='manage_orders'),  # управление заказами
    path('manage-products/', manage_products, name='manage_products'),  # управление товарами
]
