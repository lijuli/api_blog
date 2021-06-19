from django_filters.rest_framework import DjangoFilterBackend, ModelChoiceFilter, FilterSet
from django.shortcuts import get_object_or_404
from rest_framework import mixins, filters, viewsets
from api.models.title import Title
from api.models.comment import Comment
from api.models.review import Review
from api.models.category import Category
from api.models.genre import Genre
from api.permissions import AuthorCanDelete
from api.permissions import IsAdmin
from api.permissions import IsAuthorOrReadOnly
from api.permissions import IsModerator
from api.permissions import IsModeratorOrReadOnly
from api.serializers import TitleSerializer
from api.serializers import CommentSerializer
from api.serializers import ReviewSerializer
from api.serializers import CategorySerializer
from api.serializers import GenreSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        DjangoModelPermissionsOrAnonReadOnly)
from api.permissions import IsAdminOrReadOnly
from api.filters import TitleFilter


class CustomViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                    mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pagination_class = PageNumberPagination


class TitleViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and editing title instances."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination


class CategoryViewSet(CustomViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(CustomViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = (IsAuthenticatedOrReadOnly,
    #  DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = [
        IsAuthorOrReadOnly,
        IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        title_id = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return Review.objects.filter(title=title_id)

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        current_user = self.request.user
        serializer.save(author=current_user, title=title)

    def get_serializer_context(self):
        return {'title_id': self.kwargs.get('title_id'),
                'request': self.request}


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthorOrReadOnly,
        IsAuthenticatedOrReadOnly
    ]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Comment.objects.filter(review=self.kwargs.get('review_id'))

    def perform_create(self, serializer):
        # if self.request.user.is_authenticated:
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
