from django_filters import rest_framework, FilterSet
from api.models.title import Title


class GenreFilterSet(FilterSet):
    genre = rest_framework.CharFilter(
        field_name='genre__slug',
    )
    category = rest_framework.CharFilter(
        field_name='category__slug',
    )

    name = rest_framework.CharFilter(
        name='name',
        lookup_expr='icontains'
    )

    year = rest_framework.NumberFilter(
        field_name='year'
    )

    class Meta:
        model = Title
        fields = ['genre', 'category', 'name', 'year',]
