# orders/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.timezone import now
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
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # Важно: related_name='items'
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Добавляем поле price


    def __str__(self):
        return f'{self.flower.name} x {self.quantity}'

class DailyReport(models.Model):
    date = models.DateField(default=now, unique=True, verbose_name="Дата отчёта")
    total_orders = models.PositiveIntegerField(default=0, verbose_name="Количество заказов")
    total_items = models.PositiveIntegerField(default=0, verbose_name="Проданных товаров")
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Выручка")

    def __str__(self):
        return f"Отчёт за {self.date}"

    class Meta:
        verbose_name = "Ежедневный отчёт"
        verbose_name_plural = "Ежедневные отчёты"    