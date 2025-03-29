from django.core.management.base import BaseCommand
from django.utils.timezone import now
from orders.models import Order, OrderItem, DailyReport
from django.db.models import Sum

class Command(BaseCommand):
    help = "Генерация ежедневного отчёта по завершённым заказам"

    def handle(self, *args, **kwargs):
        today = now().date()
        
        # Проверяем, есть ли уже отчёт за сегодня
        if DailyReport.objects.filter(date=today).exists():
            self.stdout.write(self.style.WARNING(f"Отчёт за {today} уже существует!"))
            return

        # Фильтруем только завершённые заказы
        completed_orders = Order.objects.filter(status="completed", created_at__date=today)
        total_orders = completed_orders.count()
        total_items = OrderItem.objects.filter(order__in=completed_orders).aggregate(Sum('quantity'))['quantity__sum'] or 0
        total_revenue = completed_orders.aggregate(Sum('total_price'))['total_price__sum'] or 0

        # Создаём запись в базе
        report = DailyReport.objects.create(
            date=today,
            total_orders=total_orders,
            total_items=total_items,
            total_revenue=total_revenue
        )

        self.stdout.write(self.style.SUCCESS(f"Создан отчёт за {today}: {report.total_orders} завершённых заказов, {report.total_items} товаров, {report.total_revenue} руб."))
