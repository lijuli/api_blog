from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=['user', 'moderator', 'admin'],)

    class Meta:
        fields = ('__all__')
        model = CustomUser


class SafeCustomUserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        fields = ('__all__')
        model = CustomUser
