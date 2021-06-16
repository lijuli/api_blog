from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import mixins, filters, viewsets
from api.models.title import Title
# from api.models.comment import Comment
from api.models.review import Review
from api.models.category import Category
from api.models.genre import Genre
from api.serializers import TitleSerializer
# from api.serializers import CommentSerializer
from api.serializers import ReviewSerializer
from api.serializers import CategorySerializer
from api.serializers import GenreSerializer
from rest_framework.pagination import PageNumberPagination


class CustomViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pagination_class = PageNumberPagination


class TitleViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and editing title instances."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'genre', 'name', 'year']
    pagination_class = PageNumberPagination


class CategoryViewSet(CustomViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    lookup_field = 'slug'


class GenreViewSet(CustomViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Review.objects.filter(title=self.kwargs['title_id'])

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs['title_id'])
        serializer.save(author=self.request.user, title=title)


# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     pagination_class = PageNumberPagination
#
#     def get_queryset(self):
#         return Comment.objects.filter(review=self.kwargs['review_id'])
#
#     def perform_create(self, serializer):
#         review = get_object_or_404(Review, id=self.kwargs['review_id'])
#         serializer.save(author=self.request.user, review=review)



