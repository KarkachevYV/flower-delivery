# bot_api/management/commands/check_schema.py
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Проверяет наличие нужных полей в таблице bot_api_botuser'

    def handle(self, *args, **options):
        table_name = 'bot_api_botuser'
        expected_fields = ['id', 'telegram_id', 'username', 'first_name', 'last_name', 'created_at', 'phone_number']

        self.stdout.write(f"🔍 Проверка таблицы '{table_name}'...")

        with connection.cursor() as cursor:
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = [row[1] for row in cursor.fetchall()]

        missing = set(expected_fields) - set(columns)

        for col in expected_fields:
            if col in columns:
                self.stdout.write(self.style.SUCCESS(f"✔ Поле '{col}' найдено"))
            else:
                self.stdout.write(self.style.ERROR(f"❌ Поле '{col}' отсутствует"))

        if missing:
            self.stdout.write(self.style.WARNING("\n⚠ Обнаружены отсутствующие поля!"))
        else:
            self.stdout.write(self.style.SUCCESS("\n✅ Все нужные поля на месте."))
