from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters, viewsets
from api.models.title import Title
from api.serializers import TitleSerializer


class CustomViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    pass


class TitleViewSet(CustomViewSet):
    """A viewset for viewing and editing title instances."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'genre', 'name', 'year']
