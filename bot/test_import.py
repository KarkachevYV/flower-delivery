import sys
import os
from django.conf import settings

# Указываем Django, какие настройки использовать
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_delivery.settings')

# Инициализация Django
import django
django.setup()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bot.handlers import help, start
print(help.router)
