from rest_framework import serializers
from .models import Order, OrderItem
from catalog.models import Flower

class OrderItemSerializer(serializers.ModelSerializer):
    flower = serializers.PrimaryKeyRelatedField(queryset=Flower.objects.all())

    class Meta:
        model = OrderItem
        fields = ['flower', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created_at', 'status', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
