# flower_delivery/__init__.py
from __future__ import absolute_import, unicode_literals

# Это необходимо для корректной загрузки приложения Celery
from .flower_delivery_celery import celery_app

__all__ = ('celery_app',)
