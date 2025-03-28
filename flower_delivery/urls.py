# flower_delivery/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # маршруты для аккаунтов
    path('catalog/', include('catalog.urls')),    # маршруты для каталога
    path('orders/', include('orders.urls')),      # маршруты для заказов
    # path('custom-admin/', include('admin_panel.urls')),  # кастомная панель
    path('admin-panel/', include('admin_panel.urls')),  # маршруты для админ-панели
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)