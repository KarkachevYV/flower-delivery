# bot_api/urls.py
from django.urls import path
from bot_api.views import bot_user_handler, link_phone_view, UserListView
from .views import (
    # create_order,  # Создание заказа
    get_order_status,  # Получение статуса заказа
    get_user_info,  # Получение данных пользователя
    # get_analytics,  # Аналитика для администратора
    bot_get_order_detail
)
from . import views
from .views import OrdersByTelegramIdAPIView

urlpatterns = [
    path('users/all/', UserListView.as_view(), name='user-list'), # ← теперь доступен по /api/bot/users/all/
    path("users/", bot_user_handler, name="bot_user_create"),  # `POST` сюда создаёт нового
    path("users/<int:telegram_id>/", bot_user_handler, name="bot_user_get"),  # `GET` сюда ищет по ID
    # path("create_order/", create_order, name="create_order"),
    path("order_status/<int:order_id>/", get_order_status, name="get_order_status"),
    path('orders/', views.OrderListAPIView.as_view(), name='order-list'),    
    path('orders/by_telegram/<int:telegram_id>/', OrdersByTelegramIdAPIView.as_view(), name='orders-by-telegram'),
    path('orders/<int:order_id>/', bot_get_order_detail, name='bot-order-detail'),
    path("user_info/<int:user_id>/", get_user_info, name="get_user_info"),
    # path("analytics/", get_analytics, name="get_analytics"),
    path("link_phone/", link_phone_view, name="link_phone"),
   
]
