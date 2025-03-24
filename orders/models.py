# orders/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from accounts.models import CustomUser
from catalog.models import Flower

User = get_user_model()

ORDER_STATUS_CHOICES = [
    ('pending', 'В ожидании'),
    ('accepted', 'Принят к работе'),
    ('completed', 'Завершён'),
    ('canceled', 'Отменён')
]

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default='pending')
    updated_at = models.DateTimeField(auto_now=True)
    # Сохраняем "исторические" данные заказа
    address = models.TextField()
    phone = models.CharField(max_length=20)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Заказ #{self.id} — {self.customer.username}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.flower.name} x {self.quantity}'