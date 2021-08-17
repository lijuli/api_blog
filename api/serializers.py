from rest_framework import serializers

from api.models.category import Category
from api.models.comment import Comment
from api.models.genre import Genre
from api.models.review import Review
from api.models.title import Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        exclude = ('id',)


class TitleReadSerializer(serializers.ModelSerializer):
    rating = serializers.FloatField(read_only=True)
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

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


class TitleWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    score = serializers.IntegerField(
        min_value=1,
        max_value=10,
    )

    class Meta:
        exclude = ('title',)
        model = Review

    def validate(self, data):
        current_user_review = Review.objects.filter(
            title_id=self.context.get('title_id'),
            author=self.context.get('request').user
        )
        if (self.context.get('request').method != 'PATCH'
                and current_user_review.exists()):
            raise serializers.ValidationError(('This user has already added '
                                               'review for this title.'))
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        read_only_fields = ('review',)
        exclude = ('review',)
        model = Comment
