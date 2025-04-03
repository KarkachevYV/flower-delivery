from rest_framework import serializers
from accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    full_address = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role', 'full_address']

    def get_full_address(self, obj):
        return f"{obj.country}, {obj.region}, {obj.city}, {obj.street} {obj.house_number}, {obj.postal_code}".strip(", ")
