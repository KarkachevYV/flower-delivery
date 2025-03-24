# flower_delivery/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # маршруты для аккаунтов
    path('catalog/', include('catalog.urls')),    # маршруты для каталога
    path('orders/', include('orders.urls')),      # маршруты для заказов
    path('admin-panel/', include('admin_panel.urls')),  # маршруты для админ-панели
]
