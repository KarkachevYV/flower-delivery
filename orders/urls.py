# orders/urls.py
from django.urls import path
from . import views
from .views import export_daily_report, repeat_order
from .admin import download_pdf_report, download_excel_report


app_name = 'orders'

urlpatterns = [
    path('cart/', views.cart, name='cart'),                            # корзина
    path('add-to-cart/<int:flower_id>/', views.add_to_cart, name='add_to_cart'),  # добавить товар в корзину
    path('checkout/', views.checkout, name='checkout'),  # оформление заказа
    path('api/orders/', views.OrderViewSet.as_view({'get': 'list'}), name='order_api'),  # API для заказов
    path('order-history/', views.order_history, name='order_history'),  # история заказов
    path('repeat-order/<int:order_id>/', repeat_order, name='repeat_order'),
    path('export-daily-report/', export_daily_report, name='export_daily_report'),
    path('admin/download_pdf/', download_pdf_report, name='download_pdf_report'),
    path('admin/download_excel/', download_excel_report, name='download_excel_report'),
]

