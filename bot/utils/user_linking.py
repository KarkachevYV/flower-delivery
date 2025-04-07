# bot/utils/user_linking.py

from asgiref.sync import sync_to_async
from accounts.models import CustomUser
from bot_api.models import BotUser


@sync_to_async
def link_telegram_to_customuser(telegram_id, phone_number):
    try:
        user = CustomUser.objects.get(phone=phone_number)
        bot_user = BotUser.objects.get(telegram_id=telegram_id)
        bot_user.customuser = user
        bot_user.save()
        return True
    except CustomUser.DoesNotExist:
        return False
