# bot_api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.db.models import Sum

from accounts.models import CustomUser
from accounts.serializers import UserSerializer

from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer

from bot_api.models import BotUser
from .serializers import BotUserSerializer
from accounts.utils import normalize_phone_number

@api_view(["POST"])
def link_phone_view(request):
    telegram_id = request.data.get("telegram_id")
    phone = request.data.get("phone_number")

    if not phone or not telegram_id:
        return Response({"error": "Необходимо указать номер телефона и Telegram ID"}, status=400)

    # Нормализуем телефон
    normalized = normalize_phone_number(phone)
    print(f"📞 Входящий номер: {phone}")
    print(f"✅ Нормализованный номер: {normalized}")

    try:
        # 🔎 Отладка: выведем все номера в базе перед поиском
        all_numbers = list(CustomUser.objects.values_list("phone_number", flat=True))
        print(f"📋 Все номера в базе: {all_numbers}")

        # 🔍 Пробуем найти пользователя
        user = CustomUser.objects.get(phone_number=normalized)
        print(f"✅ Пользователь найден: {user}")

        # Привязываем номер к боту
        bot_user, _ = BotUser.objects.get_or_create(telegram_id=telegram_id)
        bot_user.phone_number = normalized
        bot_user.save()

        print(f"✅ Телефон успешно привязан к {bot_user}")
        return Response({
            "message": "Телефон успешно привязан.",
            "bot_user_id": bot_user.id,
            "site_user_id": user.id
        }, status=200)

    except CustomUser.DoesNotExist:
        # 🔍 Если не найден, пробуем через filter()
        user = CustomUser.objects.filter(phone_number=normalized).first()
        if not user:
            print(f"❌ Нет совпадения с: {normalized}")
            return Response({"error": "Пользователь с таким номером не найден"}, status=404)

        print(f"⚠️ Пользователь всё же найден через filter(): {user}")
        return Response({"error": "Пользователь с таким номером не найден"}, status=404)

class UserListView(APIView):
    def get(self, request):
        users = BotUser.objects.all()
        serializer = BotUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Получение данных о пользователе по Telegram ID
@api_view(['GET', 'POST'])
def bot_user_handler(request, telegram_id=None):
    if request.method == 'GET':
        # Получение пользователя
        try:
            user = BotUser.objects.get(telegram_id=telegram_id)
            serializer = BotUserSerializer(user)
            return Response(serializer.data)
        except BotUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

    elif request.method == 'POST':
        # Создание пользователя
        serializer = BotUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(["GET"])
def get_analytics(request):
    if not request.user.is_staff:
        return Response({"error": "Доступ запрещён"}, status=403)

    total_revenue = Order.objects.filter(status="Доставлен").aggregate(Sum("total_price"))["total_price__sum"] or 0
    top_selling = OrderItem.objects.values("product__name").annotate(total=Sum("quantity")).order_by("-total").first()

    return Response({
        "total_revenue": total_revenue,
        "top_selling": top_selling["product__name"] if top_selling else "Нет данных"
    })


@api_view(["GET"])
def get_user_info(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
def get_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return Response({"order_id": order.id, "status": order.status})


@api_view(["POST"])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Заказ создан!", "order": serializer.data}, status=201)
    return Response(serializer.errors, status=400)
