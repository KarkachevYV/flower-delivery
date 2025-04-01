# flower_delivery/flower_delivery_celery.py
from __future__ import absolute_import, unicode_literals
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

@celery_app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))