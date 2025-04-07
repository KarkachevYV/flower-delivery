from django.db import models
from django.conf import settings  # для ссылки на кастомную модель пользователя

class BotUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Добавляем внешний ключ для связи с пользователем в основной системе
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Используем кастомную модель пользователя, настроенную в settings.py
        on_delete=models.SET_NULL,  # В случае удаления пользователя, связь останется
        null=True,  # Это поле может быть пустым
        blank=True,  # Это поле может быть пустым
        related_name='telegram_profile'       # Это имя обратной связи
    )

    def __str__(self):
        return f"{self.first_name or 'Без имени'} (@{self.username})"
