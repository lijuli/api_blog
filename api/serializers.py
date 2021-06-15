from rest_framework import serializers

from api.models.title import Title


class TitleSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=500)

    class Meta:
        fields = '__all__'
        model = Title
