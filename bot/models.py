# bot/models.py

from bot_api.models import BotUser
from asgiref.sync import sync_to_async


@sync_to_async
def get_or_create_bot_user(from_user):
    obj, _ = BotUser.objects.get_or_create(
        telegram_id=from_user.id,
        defaults={
            "username": from_user.username,
            "first_name": from_user.first_name,
            "last_name": from_user.last_name,
        }
    )
    return obj
