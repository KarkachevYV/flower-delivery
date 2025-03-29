from celery import shared_task
from django.core.management import call_command
from datetime import date
from .models import Order

@shared_task
def generate_daily_report_task():
    call_command('generate_daily_report')

@shared_task
def generate_daily_report():
    today = date.today()
    completed_orders = Order.objects.filter(status='completed', created_at__date=today)

    total_revenue = sum(order.total_price for order in completed_orders)
    total_orders = completed_orders.count()

    report = f"Отчёт за {today}:\nЗавершённых заказов: {total_orders}\nВыручка: {total_revenue}₽"

    # Сохраняем в БД (можно сделать модель для отчётов)
    print(report)  # Заглушка, потом можно заменить на сохранение в БД или отправку в Telegram

    return report