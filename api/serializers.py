from rest_framework import serializers

from users.models import CustomUser
from api.models.title import Title

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = CustomUser


class TitleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=500)

    class Meta:
        fields = '__all__'
        model = Title
