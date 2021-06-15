from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

# from users.models import CustomUser
# from .serializers import CustomUserSerializer
from api.models.title import Title
from api.serializers import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and editing title instances."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'genre', 'name', 'year']


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
