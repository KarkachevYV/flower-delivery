from django.db import models

class BotUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)  # ID пользователя в Telegram
    username = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата регистрации

    def __str__(self):
        return f"{self.username} ({self.telegram_id})"

