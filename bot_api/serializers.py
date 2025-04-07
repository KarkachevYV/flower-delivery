# bot_api\serializers.py
from rest_framework import serializers
from .models import BotUser
 
class BotUserSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    user_last_name = serializers.CharField(source='user.last_name', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = BotUser
        fields = [
            'id', 'telegram_id', 'username', 'first_name', 'last_name', 'phone_number',
            'created_at', 'user',
            'user_email', 'user_first_name', 'user_last_name', 'user_username'
        ]
