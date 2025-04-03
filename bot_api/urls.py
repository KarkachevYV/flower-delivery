# bot_api/urls.py
from django.urls import path
from .views import bot_user_handler
from .views import (
    create_order,  # Создание заказа
    get_order_status,  # Получение статуса заказа
    get_user_info,  # Получение данных пользователя
    get_analytics,  # Аналитика для администратора
)
from .views import UserListView


urlpatterns = [
    path('users/all/', UserListView.as_view(), name='user-list'), # ← теперь доступен по /api/bot/users/all/
    path("users/", bot_user_handler, name="bot_user_create"),  # `POST` сюда создаёт нового
    path("users/<int:telegram_id>/", bot_user_handler, name="bot_user_get"),  # `GET` сюда ищет по ID
    path("create_order/", create_order, name="create_order"),
    path("order_status/<int:order_id>/", get_order_status, name="get_order_status"),
    path("user_info/<int:user_id>/", get_user_info, name="get_user_info"),
    path("analytics/", get_analytics, name="get_analytics"),
]
