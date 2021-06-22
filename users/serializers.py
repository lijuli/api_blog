from rest_framework import serializers

from users.models import CustomUser, Roles


class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Roles.values)

    class Meta:
        fields = ('__all__')
        model = CustomUser


class SafeCustomUserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        fields = ('__all__')
        model = CustomUser


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class TokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)
