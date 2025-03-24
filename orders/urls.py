# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order-history/', views.order_history, name='order_history'),  # история заказов
    path('cart/', views.cart, name='cart'),                            # корзина
    path('add-to-cart/<int:flower_id>/', views.add_to_cart, name='add_to_cart'),  # добавить товар в корзину
    path('checkout/', views.checkout, name='checkout'),  # оформление заказа
    path('api/orders/', views.OrderViewSet.as_view({'get': 'list'}), name='order_api'),  # API для заказов
]
