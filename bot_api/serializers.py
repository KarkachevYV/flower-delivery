from rest_framework import serializers
from .models import BotUser
 
class BotUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotUser
        fields = '__all__'  # Все поля модели
