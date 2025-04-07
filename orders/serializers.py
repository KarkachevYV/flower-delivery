# orders\serializers.py
from rest_framework import serializers
from .models import Order, OrderItem, Review
from catalog.models import Flower

class OrderItemSerializer(serializers.ModelSerializer):
    flower = serializers.PrimaryKeyRelatedField(queryset=Flower.objects.all())


    class Meta:
        model = OrderItem
        fields = ['flower', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    address = serializers.SerializerMethodField()  # Восстанавливаем поле
    phone = serializers.CharField(source='customer.phone_number', read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id',
            'customer',
            'created_at',
            'status',
            'items',
            'total_price',
            'address',
            'phone'
        ]

    def get_address(self, obj):
        # Если адрес явно указан — показываем его
        if obj.address:
            return obj.address

        # Иначе собираем адрес из профиля пользователя
        user = obj.customer
        parts = [
            user.postal_code,
            user.country,
            user.region,
            user.city,
            user.street,
            user.house_number
        ]
        return ', '.join(filter(None, parts)) or 'Адрес не указан'

    def get_total_price(self, obj):
        try:
            return sum((item.price or 0) * item.quantity for item in obj.items.all())
        except Exception as e:
            print("Ошибка при вычислении total_price:", e)
            return 0

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = validated_data['customer']

        # Если адрес не указан, заполняем из профиля
        if not validated_data.get('address'):
            validated_data['address'] = ', '.join(filter(None, [
                user.postal_code,
                user.country,
                user.region,
                user.city,
                user.street,
                user.house_number
            ]))

        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'order', 'rating', 'text', 'created_at']