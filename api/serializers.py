from django.db.models import Avg
from api.models.review import Review
from rest_framework import serializers

from api.models.title import Title
# from api.models.comment import Comment
from api.models.category import Category
from api.models.genre import Genre


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category'
        )
        model = Title

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = CategorySerializer(instance.category).data
        response['genre'] = GenreSerializer(instance.genre, many=True).data
        return response

    def get_rating(self, obj):
        return obj.review.all().aggregate(Avg('score')).get('score__avg')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = '__all__'
        model = Genre
        fields = (
            'name',
            'slug',
        )


class ReviewSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='username',
    #     # default=serializers.CurrentUserDefault()
    # )

    class Meta:
        fields = '__all__'
        read_only_fields = ('title',)
        model = Review


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field='username'
#     )
#
#     class Meta:
#         fields = '__all__'
#         read_only_fields = ('review',)
#         model = Comment
