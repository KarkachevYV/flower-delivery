import os
from celery import Celery

import django
django.setup()

from django_celery_beat.models import PeriodicTask, IntervalSchedule

# Указываем Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_delivery.settings')

# Создаём объект Celery
celery_app = Celery('flower_delivery')

# Загружаем настройки из Django settings
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим задачи во всех приложениях
celery_app.autodiscover_tasks()
